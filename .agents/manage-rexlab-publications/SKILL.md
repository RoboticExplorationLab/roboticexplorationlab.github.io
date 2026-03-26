---
name: manage-rexlab-publications
description: Add or update publication entries for the Robotic Exploration Lab website. Use when Codex needs to add a paper to `_data/pubs.yml`, update publication metadata such as `status`, `pdf` or arXiv links, `venue`, `publisher`, `abbrv`, or linked `projects`, or create or update an associated project page under `_projects/` for the Research section while keeping publication and project keys consistent.
---

# Manage REx Lab Publications

Add or update publication metadata in `_data/pubs.yml`, and create or edit linked research project pages when needed. Prefer minimal, localized edits and keep publication/project keys consistent.

## Required Information

Always require enough information to identify the publication:

- Existing paper: the exact title or an unambiguous match in `_data/pubs.yml`
- New paper: `title`, `authors`, `publisher`, `date`, `pub-type`, and `pdf`

Optional publication fields:

- `abbrv`
- `venue`
- `status`
- `projects`

Only require project-page details when the user asks for a research/project page or the request clearly says to add/update `_projects/<slug>.md`:

- `project key`
- `title`
- `description`
- `people`
- `last-updated`

Optional project-page fields:

- `image`
- `link`
- `no-link`
- page body content

If any required information is missing, ask a concise clarifying follow-up before editing. Ask only for the missing fields. Do not guess author spellings, project keys, dates, statuses, or arXiv/PDF links.

## Workflow

1. Read [references/repo-layout.md](./references/repo-layout.md) before editing.
2. Inspect `_data/pubs.yml` to determine whether the request is a new publication or an update to an existing one.
3. For status/link-only updates, patch only the changed fields on the matching publication entry.
4. For new publications, append a new YAML list item to the bottom of `_data/pubs.yml`. The public page sorts by `date`, so append-only diffs are acceptable and easier to review.
5. Keep publication fields in the existing house style and usual order when present: `title`, `authors`, `publisher`, `abbrv`, `pub-type`, `date`, `venue`, `pdf`, `projects`, `status`.
6. Omit blank fields instead of leaving empty keys in `_data/pubs.yml`.
7. Use `pdf:` for both local filenames and external URLs. If the value contains `http`, the site links directly; otherwise it resolves under `/papers/`.
8. Authors may mix `_data/people.yml` keys and literal names. Keep existing person keys when available.
9. Only ask about a linked project page if the request explicitly mentions the Research page, `_projects`, or a `projects` key that should point to a project page.
10. If a project page is needed, ensure `projects: [project_key]` in `_data/pubs.yml` matches `_projects/<project_key>.md`.
11. When creating a new `_projects/<project_key>.md`, start from [assets/project-page-template.md](./assets/project-page-template.md) and replace every placeholder.
12. Make sure `people:` keys on project pages exist in `_data/people.yml`.
13. Do not edit `bib/pubs.bib` or `_includes/pubs.html` unless the user explicitly asks for the BibTeX pipeline.

## Validation

- Run:

```bash
ruby -e "require 'yaml'; YAML.load_file('_data/pubs.yml'); puts 'pubs.yml OK'"
```

- If you created or edited a project page, also validate its front matter by inspection.
- When the local toolchain is available, run `make build` or `make serve`.
- If build tooling is missing, say that explicitly and rely on YAML validation plus diff review.

## Notes

- `_data/pubs.yml` is the source this skill should edit for website publication entries.
- `bib/pubs.bib` exists, but do not switch workflows unless the user explicitly asks.
- New project pages should use short, lowercase filenames such as `_projects/trajectory_bundle.md`.
- Keep diffs localized and avoid reformatting unrelated publication entries.
