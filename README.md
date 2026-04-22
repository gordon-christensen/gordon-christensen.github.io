# Rutabaga Yoga — Jekyll theme

A small, hand-built Jekyll theme for [rutabaga-yoga.org](https://rutabaga-yoga.org).
Matched to the Rutabaga Yoga brand — deep aubergine, cream, gold accent,
and a rutabaga mark for a logo.

## Run locally

```bash
bundle install
bundle exec jekyll serve
```

Open <http://localhost:4000>.

## Deploy to GitHub Pages

1. Push this repo to GitHub (e.g., `yourname/rutabaga-yoga`).
2. In **Settings → Pages**, set **Source** to `Deploy from a branch`, branch `main`, folder `/ (root)`.
3. Point your domain: create a file called `CNAME` at the repo root containing `rutabaga-yoga.org`, and configure DNS per
   [GitHub's custom-domain docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site).

## Writing a post

Add a file under `_posts/` named `YYYY-MM-DD-slug.md`:

```markdown
---
layout: post
title:  "On stillness"
date:   2026-04-20
excerpt: A short prelude line that shows up in the archive.
---

Body text in Markdown.
```

## Editing the nav / site info

Everything user-visible lives in `_config.yml` (titles, tagline, nav links,
email). Content pages are in the repo root (`about.md`, `contact.md`).

## Colors / typography

All design tokens live at the top of `assets/css/main.scss` as CSS variables.
Edit there and every page updates.
