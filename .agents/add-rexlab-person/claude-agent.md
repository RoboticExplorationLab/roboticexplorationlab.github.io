---
name: add-rexlab-person
description: Add or update people entries for the Robotic Exploration Lab website. Use when a request involves adding a new faculty member, postdoc, visitor, staff member, student, alumnus, or collaborator; updating a person's bio, links, or image path; moving someone between roles; or creating a new People-page role section while keeping `_data/people.yml`, `_config.yml`, `people.html`, and `img/people/` consistent.
---

# Add REx Lab Person

Add or update a person on the REx Lab website with minimal manual editing. Use the repo-local helper script for repeatable changes, then review the diff and run lightweight validation.

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

## Workflow

1. Confirm the repo root contains `_data/people.yml`, `_config.yml`, and `people.html`.
2. Gather the required fields, then collect optional `webpage` and `github` values if they exist.
3. If the role is brand new, also gather `role-label`, `insert-after-role`, and `group`.
4. If the image is not already in the repo, provide a source file path and let the script copy it into place.
5. Run:

```bash
python3 .agents/add-rexlab-person/scripts/upsert_person.py \
  --repo /path/to/repo \
  --key joris \
  --display-name "Joris Verhagen" \
  --role visitor \
  --bio "Continuous and discrete optimization for temporal logic planning" \
  --image /img/people/joris.jpeg
```

6. If the role is new, also pass `--role-label`, `--insert-after-role`, and `--group`.
7. New people must be appended at the bottom of `_data/people.yml`; existing people should be updated in place.
8. Review the diff to make sure only the intended person block and role placement changed.

## Validation

- Run:

```bash
ruby -e "require 'yaml'; YAML.load_file('_data/people.yml'); puts 'people.yml OK'"
```

- When the local toolchain is available, run `make build` or `make serve`.
- If build tooling is missing, say that explicitly and rely on the YAML check plus diff review.

## References

- Repo notes: `./.agents/add-rexlab-person/references/repo-layout.md`
- Helper script: `./.agents/add-rexlab-person/scripts/upsert_person.py`
