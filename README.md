# Diela website

Complete source and assets for **Diela — Connected skincare**, exported from the latest ChatGPT Sites source on 21 October 2026.

## Run locally

Requires Python 3; no JavaScript dependencies are needed.

```sh
python3 src/build.py
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000.

## Project structure

- `src/` — editable HTML, CSS, JavaScript, app interface excerpts, and original artwork.
- `dist/` — ready-to-serve website, including local images, fonts, and font licenses.
- `design/` — implementation notes and design reference previews.
- `.openai/hosting.json` — existing ChatGPT Sites configuration.

The main build inputs are `src/diela-editorial.html`, `src/editorial.css`, `src/dawn.css`, `src/editorial.js`, and selected fragments in `src/native/`. Rebuild after editing them.

## Hosting and handoff

Serve `dist/` as the static website directory. The current testing-list links point to the original Diela Site's registration form; review that destination before hosting under a new domain. The exported site retains its existing noindex setting.

This repository contains the website, not the full Diela application or registration backend. Runtime data, credentials, and visitor submissions are not included. See `design/README.md` for implementation history and verification limits.
