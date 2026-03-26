# REx Lab Publication Update Notes

Relevant files:

- `_data/pubs.yml`: source of truth for publication entries shown on `publications.html`
- `_includes/pub_entry.html`: publication rendering rules
- `_projects/<key>.md`: optional research/project pages linked from publication `projects`
- `_layouts/project.html`: related-paper lookup for project pages
- `publications.html`: sorts publications by `date` descending at render time

Publication entry conventions:

- Use a YAML list item starting with `- title:`.
- Usual field order when present:
  - `title`
  - `authors`
  - `publisher`
  - `abbrv`
  - `pub-type`
  - `date`
  - `venue`
  - `pdf`
  - `projects`
  - `status`
- Append new entries to the bottom of `_data/pubs.yml`; render order is controlled by `date`.
- Omit empty fields instead of leaving blank keys.

Field semantics:

- `authors` may mix `_data/people.yml` keys and literal strings.
- `pdf` may be either:
  - a local filename like `tinympc_cdc24.pdf`, which renders as `/papers/<filename>`
  - a full external URL such as an arXiv link
- `projects` is a list of project keys. Each key should match the basename of `_projects/<key>.md`.
- `status` is optional and rendered in parentheses.

Project-page conventions:

- Use lowercase filenames like `_projects/trajectory_bundle.md`.
- Typical front matter includes:
  - `title`
  - `description`
  - `people`
  - `layout: project`
  - `image`
  - `last-updated`
- `people` values must be keys from `_data/people.yml`.
- The project page body is freeform markdown. It often includes a paper link and a resources section.

Do not edit these unless the user explicitly asks:

- `bib/pubs.bib`
- `_includes/pubs.html`
