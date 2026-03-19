# Repository Guidelines

## Project Structure & Module Organization
This repository is a Jekyll-based lab website. Top-level pages such as `index.html`, `people.html`, `research.html`, and `publications.html` define the main site routes. Reusable templates live in `_layouts/` and `_includes/`. Structured content is stored in `_projects/` for research pages, `_posts/` for news/blog entries, and `_data/` for YAML-backed site data such as `_data/people.yml`. Static assets belong in `img/`, `papers/`, `css/`, and `js/`. Bibliography source files live in `bib/`; generated publication markup is written to `_includes/pubs.html`.

## Build, Test, and Development Commands
Use `make` or `make build` to regenerate publications and build the site into `_site/`. Use `make serve` to start a local preview on `http://127.0.0.1:5000`; override the port with `SERVE_PORT=4000 make serve` if needed. Use `make clean` to remove `_site/` and the generated publications include. Jekyll and the local BibTeX pipeline are the only required build steps here.

## Coding Style & Naming Conventions
Match the existing formatting in each file type: HTML and SCSS use 4-space indentation, and YAML entries in `_data/` are also indented consistently. Keep Markdown front matter minimal and explicit. New posts must follow `YYYY-MM-DD-title.md`; new project files should use short, lowercase filenames such as `_projects/tinympc.md`. Reuse existing data keys in `_data/people.yml` when assigning project contributors.

## Testing Guidelines
There is no dedicated automated test suite in this repository. Validate changes by running `make` to catch Jekyll or bibliography errors, then `make serve` and manually inspect affected pages, navigation links, images, and publication entries. For content changes, verify both the source file and the rendered page.

## Commit & Pull Request Guidelines
Recent commit messages are short and direct, for example `calendar update`, `MIT updates`, and `Move Swami and Paulo to alumni`. Follow that pattern: concise, descriptive summaries focused on the visible change. Pull requests should include a brief description, list the pages or data files touched, reference any related issue, and attach screenshots for layout or styling changes.
