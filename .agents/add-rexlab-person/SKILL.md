---
name: add-rexlab-person
description: Add or update people entries for the Robotic Exploration Lab website. Use when Codex needs to add a new faculty member, postdoc, visitor, staff member, student, alumnus, or collaborator; update a person's bio, links, or image path; move someone between roles; or create a new People-page role section while keeping `_data/people.yml`, `_config.yml`, `people.html`, and `img/people/` consistent.
---

# Add REx Lab Person

Add or update a person on the REx Lab website with minimal manual editing. Prefer the helper script for repeatable changes, then review the diff and run lightweight validation.

## Quick Start

1. Confirm the repo root contains `_data/people.yml`, `_config.yml`, and `people.html`.
2. Gather the required fields: person key, full name, role, bio, and final image path under `img/people/`.
3. Gather optional fields if they exist: `webpage` and `github`. Do not block on either one.
4. Only if the provided role is missing from the repo's existing roles, gather `role-label`, `insert-after-role`, and `group`.
5. Before asking for image details, inspect repo changes for a plausible new or modified profile image under `img/people/`.
6. If a changed file under `img/people/` plausibly matches the person's name or key, use that repo-relative path as the image.
7. If no plausible image is already present in repo changes, ask the user to add a profile photo under `img/people/` and provide the filename or path.
8. Do not run the script until every required field is available.
9. Run `scripts/upsert_person.py` from this skill.

## Required Information

Always require:

- `key`
- `display-name`
- `role`
- `bio`
- `image`

Conditionally require only when the provided role is not already present in `_config.yml` or `people.html`:

- `role-label`
- `insert-after-role`
- `group`

If any required information is missing, ask a concise clarifying follow-up before running the script. Ask only for the missing fields, bundle them into one short question when possible, and keep following up until all required information is present. `webpage` and `github` are optional and should not block the workflow. Before asking for an image path, first check repo changes for a plausible new file under `img/people/`. Do not proactively ask whether the role is brand new; first check the repo's existing roles. Do not invent placeholder bios, keys, image paths, or role placement details.

## Use The Script

Use the helper script at [scripts/upsert_person.py](./scripts/upsert_person.py) for most changes:

```bash
python3 .agents/add-rexlab-person/scripts/upsert_person.py \
  --repo /path/to/repo \
  --key joris \
  --display-name "Joris Verhagen" \
  --role visitor \
  --bio "Continuous and discrete optimization for temporal logic planning" \
  --image /img/people/joris.jpeg
```

If the role already exists, the script updates the existing person entry in place unless the role is missing from `people.html`.

If the person is new, the script appends that entry to the bottom of `_data/people.yml`.

If the role is not already present in the repo, also pass:

- `--role-label "Visitors"` to add the heading label in `_config.yml`
- `--insert-after-role postdoc` to place the new role after an existing one
- `--group picture` or `--group no-picture` to place the role in the correct section of `people.html`

Example for a new `visitor` role between `postdoc` and `staff`:

```bash
python3 .agents/add-rexlab-person/scripts/upsert_person.py \
  --repo /path/to/repo \
  --key joris \
  --display-name "Joris Verhagen" \
  --role visitor \
  --role-label "Visitors" \
  --insert-after-role postdoc \
  --group picture \
  --bio "Continuous and discrete optimization for temporal logic planning" \
  --image /img/people/joris.jpeg \
  --copy-image-from /path/to/joris.jpeg
```

## Workflow

1. Use the repo notes in [references/repo-layout.md](./references/repo-layout.md) if you need a reminder about the relevant files and current section order.
2. Check repo changes before asking for image information. Inspect `git diff --name-only -- img/people`, `git diff --cached --name-only -- img/people`, and untracked files under `img/people/`.
3. If there is a plausible changed image whose basename matches the person's name or key, use that repo-relative path, for example `/img/people/joris.jpeg`.
4. Otherwise, ask the user to add a profile photo under `img/people/` and tell you the filename or path.
5. Prefer lowercase identifiers for `--key`, using underscores when needed, such as `patrick_mckeen`.
6. Treat `webpage` and `github` as optional. Ask for them only if they are useful and missing, but do not block on them.
7. Do not ask for `role-label`, `insert-after-role`, or `group` unless the provided role is missing from the repo's existing roles.
8. Run the script once with the final values instead of editing multiple files by hand.
9. Review the diff to make sure only the intended person block and role placement changed.

## Validation

- Run:

```bash
ruby -e "require 'yaml'; YAML.load_file('_data/people.yml'); puts 'people.yml OK'"
```

- When the local toolchain is available, run `make build` or `make serve`.
- If build tooling is missing, say that explicitly and rely on the YAML check plus diff review.

## Notes

- Do not reorder unrelated entries in `_data/people.yml`.
- New people must be appended at the bottom of `_data/people.yml`.
- `webpage` and `github` are optional.
- Before asking for an image path, check repo changes under `img/people/` for a plausible matching file.
- Do not proactively ask whether a role is new; check the repo's existing roles first.
- Do not invent new role headings unless the user requests a new section.
- Keep the skill repo-specific. It assumes the REx Lab site structure and file names.
