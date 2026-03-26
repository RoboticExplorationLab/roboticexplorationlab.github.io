---
name: add-rexlab-person
description: Add or update people entries for the Robotic Exploration Lab website. Use when Codex needs to add a new faculty member, postdoc, visitor, staff member, student, alumnus, or collaborator; update a person's bio, links, or image path; move someone between roles; or create a new People-page role section while keeping `_data/people.yml`, `_config.yml`, `people.html`, and `img/people/` consistent.
---

# Add REx Lab Person

Add or update a person on the REx Lab website with minimal manual editing. Prefer the helper script for repeatable changes, then review the diff and run lightweight validation.

## Quick Start

1. Confirm the repo root contains `_data/people.yml`, `_config.yml`, and `people.html`.
2. Gather the required fields: person key, full name, role, bio, and final image path under `img/people/`.
3. Gather optional fields if they exist: `webpage` and `github`.
4. If the role is brand new, also gather `role-label`, `insert-after-role`, and `group`.
5. If the image is not already in the repo, provide a source file path and let the script copy it into place.
6. Do not run the script until every required field is available.
7. Run `scripts/upsert_person.py` from this skill.

## Required Information

Always require:

- `key`
- `display-name`
- `role`
- `bio`
- `image`

Conditionally require for a new role:

- `role-label`
- `insert-after-role`
- `group`

If any required information is missing, ask a concise clarifying follow-up before running the script. Ask only for the missing fields, bundle them into one short question when possible, and keep following up until all required information is present. Do not invent placeholder bios, keys, image paths, or role placement details.

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

If the role is new, also pass:

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
2. Put new photos under `img/people/` and keep the YAML image path repo-relative, for example `/img/people/joris.jpeg`.
3. Prefer lowercase identifiers for `--key`, using underscores when needed, such as `patrick_mckeen`.
4. Run the script once with the final values instead of editing multiple files by hand.
5. Review the diff to make sure only the intended person block and role placement changed.

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
- Do not invent new role headings unless the user requests a new section.
- Keep the skill repo-specific. It assumes the REx Lab site structure and file names.
