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

Conditionally require only when the provided role is not already present in `_config.yml` or `people.html`:

- `role-label`
- `insert-after-role`
- `group`

If any required information is missing, ask a concise clarifying follow-up before running the script. Ask only for the missing fields, bundle them into one short question when possible, and keep following up until all required information is present. `webpage` and `github` are optional and should not block the workflow. Before asking for an image path, first check repo changes for a plausible new file under `img/people/`. Do not proactively ask whether the role is brand new; first check the repo's existing roles. Do not invent placeholder bios, keys, image paths, or role placement details.

## Workflow

1. Confirm the repo root contains `_data/people.yml`, `_config.yml`, and `people.html`.
2. Gather the required fields, then collect optional `webpage` and `github` values if they exist. Do not block on either one.
3. Only if the provided role is missing from the repo's existing roles, gather `role-label`, `insert-after-role`, and `group`.
4. Check repo changes before asking for image information. Inspect changed and untracked files under `img/people/`.
5. If there is a plausible changed image whose basename matches the person's name or key, use that repo-relative path.
6. Otherwise, ask the user to add a profile photo under `img/people/` and tell you the filename or path.
7. Run:

```bash
python3 .agents/add-rexlab-person/scripts/upsert_person.py \
  --repo /path/to/repo \
  --key joris \
  --display-name "Joris Verhagen" \
  --role visitor \
  --bio "Continuous and discrete optimization for temporal logic planning" \
  --image /img/people/joris.jpeg
```

8. If the role is not already present in the repo, also pass `--role-label`, `--insert-after-role`, and `--group`.
9. New people must be appended at the bottom of `_data/people.yml`; existing people should be updated in place.
10. Review the diff to make sure only the intended person block and role placement changed.

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
