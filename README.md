# Eitan Lees Blog

This repository is an old Jekyll blog for [https://eitanlees.github.io](https://eitanlees.github.io).

## Quick Start

From the repository root:

```bash
bundle install
bundle exec jekyll serve
```

Then open:

- [http://localhost:4000](http://localhost:4000)

Useful variants:

```bash
# Preview drafts too
bundle exec jekyll serve --drafts

# Build once without running the local server
bundle exec jekyll build
```

Notes:

- The generated site is written to `_site/`.
- If you change `_config.yml`, restart `jekyll serve`.
- If `bundle` or Ruby is missing, install Ruby and Bundler first, then come back here.

## Repo Layout

- `_posts/`: published blog posts
- `_drafts/`: unpublished drafts
- `notebooks/`: source Jupyter notebooks for some older posts
- `notebooks/*_files/`: generated notebook figures referenced by posts
- `assets/`: images and styles
- `_includes/`: custom Jekyll includes
- `_config.yml`: site configuration
- `Gemfile`: Ruby dependencies for local development

## How Posting Worked

There are two main workflows in this repo.

### 1. Plain Markdown Posts

1. Create a draft in `_drafts/`.
2. Preview locally with `bundle exec jekyll serve --drafts`.
3. When ready, move/rename it into `_posts/` using Jekyll's date-based naming convention:

```text
YYYY-MM-DD-title.md
```

Example:

```text
_posts/2026-04-22-new-post.md
```

### 2. Notebook-Backed Posts

Some older posts were written from Jupyter notebooks in `notebooks/`.

Examples:

- `notebooks/scipy-stats.ipynb` -> `_posts/2018-04-04-scipy-stats.md`
- `notebooks/numpy-poly-fit.ipynb` -> `_posts/2018-04-09-numpy-poly-fit.md`

The notebook figures live in folders like:

```text
notebooks/scipy-stats_files/
```

This process is still a undocumented and I plan to come back to better
explain the process.

To convert the notebook to markdown I ran

```bash
jupyter nbconvert --to markdown nump-poly-fit-redux.ipynb 
```

Then I need to add the header to the markdown manually

```
---
layout : post
title : Numpy Polynomial Fitting Redux
permalink : /numpy-poly-fit-redux/
---
```

Remove the h1 header from the markdown as well.

Make sure the banner image is the first element after the config to have it show up in the feed.

Then I went through the markdown manually and cleaned some things up.

- Adjust the image paths for the figures
- Remove the plotting object line after a plotting cells.
- Check the mathematics and cleaning things up as needed.

## Minimal Post Template

```markdown
---
layout: post
title: "My New Post"
date: 2026-04-22
categories: misc
permalink: /my-new-post/
---

Write here.
```

Notes:

- `layout: post` is the normal post layout.
- `permalink` is optional, but many posts in this repo use it.
- `categories` is optional.
- The filename date matters for published posts in `_posts/`.

## Publishing Reminder

Historically this repo was set up like a GitHub Pages site. The site URL in `_config.yml` is:

- [https://eitanlees.github.io](https://eitanlees.github.io)

So the normal flow was likely:

1. Write locally.
2. Preview locally.
3. Commit and push.
4. Let GitHub Pages rebuild the site.
