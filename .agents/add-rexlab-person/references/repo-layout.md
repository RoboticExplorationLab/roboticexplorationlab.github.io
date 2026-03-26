# REx Lab People Update Notes

Relevant files:

- `_data/people.yml`: source of truth for names, roles, bios, links, and image paths
- `_config.yml`: heading labels for the People page
- `people.html`: section grouping and order for picture and no-picture roles
- `img/people/`: profile photos

Current People page order:

- Picture groups: `faculty`, `postdoc`, `visitor`, `staff`
- Picture groups: `phd`, `masters`, `ugrad`
- No-picture groups: `collab`, `ugrad-alum`
- No-picture groups: `alum`

Treat those role keys as the normal existing roles. Only ask for new-role placement details if the provided role is not already in this list or in `_config.yml`.

Expected person fields:

- `display_name`
- `webpage`
- `github`
- `role`
- `image`
- `bio`

Conventions:

- Use lowercase keys with digits, underscores, or hyphens.
- Keep image paths repo-relative, usually `/img/people/<filename>`.
- Match existing indentation: 4 spaces in YAML content blocks.
- `webpage` and `github` are optional.
- Before asking the user for an image path, check changed and untracked files under `img/people/` for a plausible matching filename.
- For new roles, add the heading to `_config.yml` and insert the role into the correct list in `people.html`.
