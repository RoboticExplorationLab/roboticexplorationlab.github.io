#!/usr/bin/env python3
"""Add or update a person entry for the REx Lab website."""

import argparse
import re
import shutil
import sys
from pathlib import Path


REQUIRED_REPO_FILES = ("_config.yml", "people.html", "_data/people.yml")


def fail(message):
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(1)


def yaml_quote(value):
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def render_field(name, value, prefer_plain=False):
    if value is None or value == "":
        return f"    {name}:"
    if prefer_plain and re.fullmatch(r"[A-Za-z0-9_./:-]+", value):
        rendered = value
    else:
        rendered = yaml_quote(value)
    return f"    {name}: {rendered}"


def build_person_block(args):
    lines = [
        f"{args.key}:",
        render_field("display_name", args.display_name),
        render_field("webpage", args.webpage),
        render_field("github", args.github, prefer_plain=True),
        render_field("role", args.role, prefer_plain=True),
        render_field("image", args.image, prefer_plain=True),
        render_field("bio", args.bio),
    ]
    return "\n".join(lines) + "\n\n"


def parse_top_level_keys(text):
    return list(re.finditer(r"(?m)^([A-Za-z0-9_-]+):\s*$", text))


def upsert_people_file(path, args):
    text = path.read_text()
    block = build_person_block(args)
    matches = parse_top_level_keys(text)

    for index, match in enumerate(matches):
        if match.group(1) != args.key:
            continue
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        path.write_text(text[:start] + block + text[end:])
        return "updated"

    # Keep new people at the end of the file so additions are easy to review.
    if text.rstrip():
        new_text = text.rstrip("\n") + "\n\n" + block
    else:
        new_text = block
    path.write_text(new_text)
    return "added_at_bottom"


def role_exists_in_config(text, role):
    return re.search(rf"(?m)^  - key: {re.escape(role)}\s*$", text) is not None


def ensure_role_in_config(path, role, role_label, insert_after_role):
    text = path.read_text()
    if role_exists_in_config(text, role):
        return False
    if not role_label:
        fail(f"role '{role}' is missing from _config.yml; pass --role-label")

    lines = text.splitlines(keepends=True)
    insert_at = None
    for index, line in enumerate(lines):
        match = re.match(r"^  - key: ([A-Za-z0-9_-]+)\s*$", line)
        if not match:
            continue
        if insert_after_role and match.group(1) == insert_after_role:
            insert_at = index + 2
            break

    if insert_at is None:
        if insert_after_role:
            fail(f"could not find role '{insert_after_role}' in _config.yml")
        role_lines = [
            index
            for index, line in enumerate(lines)
            if re.match(r"^  - key: [A-Za-z0-9_-]+\s*$", line)
        ]
        if not role_lines:
            fail("could not locate the roles block in _config.yml")
        insert_at = role_lines[-1] + 2

    lines[insert_at:insert_at] = [
        f"  - key: {role}\n",
        f"    name: {role_label}\n",
    ]
    path.write_text("".join(lines))
    return True


def role_exists_in_people_page(text, role):
    return re.search(rf"(?<![A-Za-z0-9_-]){re.escape(role)}(?![A-Za-z0-9_-])", text) is not None


def ensure_role_in_people_page(path, role, insert_after_role, group):
    text = path.read_text()
    if role_exists_in_people_page(text, role):
        return False
    if not insert_after_role or not group:
        fail(
            f"role '{role}' is missing from people.html; pass --insert-after-role and --group"
        )

    lines = text.splitlines(keepends=True)
    current_group = None
    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped == "picture-role-groups:":
            current_group = "picture"
            continue
        if stripped == "no-picture-role-groups:":
            current_group = "no-picture"
            continue

        if current_group != group or "roles:" not in line or "[" not in line or "]" not in line:
            continue

        match = re.search(r"\[([^\]]*)\]", line)
        if not match:
            continue
        roles = [item.strip() for item in match.group(1).split(",") if item.strip()]
        if insert_after_role not in roles:
            continue
        roles.insert(roles.index(insert_after_role) + 1, role)
        lines[index] = line[: match.start(1)] + ", ".join(roles) + line[match.end(1) :]
        path.write_text("".join(lines))
        return True

    fail(f"could not place role '{role}' after '{insert_after_role}' in people.html")


def maybe_copy_image(repo_path, image_path, source_path):
    if not source_path:
        return None

    source = Path(source_path).expanduser().resolve()
    if not source.exists():
        fail(f"image source does not exist: {source}")

    destination = (repo_path / image_path.lstrip("/")).resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    if source == destination:
        return destination

    shutil.copy2(source, destination)
    return destination


def validate_args(args):
    if not re.fullmatch(r"[a-z0-9_-]+", args.key):
        fail("--key must use lowercase letters, digits, underscores, or hyphens")
    if not re.fullmatch(r"[a-z0-9-]+", args.role):
        fail("--role must use lowercase letters, digits, or hyphens")
    if not args.image.startswith("/img/people/"):
        fail("--image must be a repo-relative path under /img/people/")


def ensure_repo_layout(repo_path):
    missing = [path for path in REQUIRED_REPO_FILES if not (repo_path / path).exists()]
    if missing:
        fail(f"repo is missing expected files: {', '.join(missing)}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Add or update a person entry for the REx Lab website."
    )
    parser.add_argument("--repo", required=True, help="Path to the repository root")
    parser.add_argument("--key", required=True, help="YAML key for the person entry")
    parser.add_argument("--display-name", required=True, help="Full display name")
    parser.add_argument("--role", required=True, help="Role key, for example visitor")
    parser.add_argument("--bio", required=True, help="Short bio shown on the people page")
    parser.add_argument("--image", required=True, help="Repo-relative image path")
    parser.add_argument("--webpage", help="Optional personal webpage URL")
    parser.add_argument("--github", help="Optional GitHub username")
    parser.add_argument(
        "--copy-image-from",
        help="Optional filesystem path to copy into the repo image location",
    )
    parser.add_argument(
        "--role-label",
        help="Heading label to add to _config.yml when the role does not yet exist",
    )
    parser.add_argument(
        "--insert-after-role",
        help="Existing role after which the new role should be inserted",
    )
    parser.add_argument(
        "--group",
        choices=("picture", "no-picture"),
        help="Which people.html group should contain the role",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    validate_args(args)

    repo_path = Path(args.repo).expanduser().resolve()
    ensure_repo_layout(repo_path)

    copied_image = maybe_copy_image(repo_path, args.image, args.copy_image_from)
    config_changed = ensure_role_in_config(
        repo_path / "_config.yml", args.role, args.role_label, args.insert_after_role
    )
    page_changed = ensure_role_in_people_page(
        repo_path / "people.html", args.role, args.insert_after_role, args.group
    )
    people_result = upsert_people_file(repo_path / "_data/people.yml", args)

    if people_result == "added_at_bottom":
        print(f"people.yml: added entry '{args.key}' at bottom")
    else:
        print(f"people.yml: updated entry '{args.key}'")
    print(f"_config.yml: {'updated' if config_changed else 'no change'}")
    print(f"people.html: {'updated' if page_changed else 'no change'}")
    if copied_image:
        print(f"image copied to: {copied_image}")



if __name__ == "__main__":
    main()
