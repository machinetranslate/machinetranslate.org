*This README is for machinetranslate.org infrastructure, not Machine Translate content.*

*For the Machine Translate landing page, visit **[index.md](index.md)**!*

### Infrastructure

The machinetranslate.org technology stack:
- Website: Jekyll
- Theme: Just the Docs
- CDN: GitHub Pages
- DNS: Cloudflare

### Running Jekyll locally

Follow the [Jekyll Quickstart Instructions](https://jekyllrb.com/docs/#instructions):

Jekyll requires Ruby version 2.5 or later, but as of July 2023, Ruby version 3.2 was too new, it had incompatibilities.

> 1. Install all [prerequisites](https://jekyllrb.com/docs/installation/).
> 2. Install the jekyll and bundler [gems](https://jekyllrb.com/docs/ruby-101/#gems).
> ```sh
> gem install jekyll bundler
> ```
> ...
> 5. Build the site and make it available on a local server.
> ```sh
> bundle exec jekyll serve
> ```
> 6. Browse to [http://localhost:4000](http://localhost:4000)

### Running generation locally

May types of articles, like languages and APIs, are generated from data files in the [`_data/`](/_data) directory.

To regenerate the articles after making a change to the data, you should run 
```
python generate.py
```


### Paths

This repository has a directory structure, to keep it orderly, but on the website the page paths are flat, to have nice page URLs.

> GitHub repository: `/quality/quality-estimation.md`
> machinetranslate.org: `/quality-estimation` (`https://machinetranslate.org/quality-estimation`)

How it works:
- In the source content on GitHub, absolute paths are used (e.g. `/quality/quality-estimation.md`).
- Jekyll removes the file extension (`.md`) - both locally and in production.
- A Cloudflare Page Rule is configured to remove the directory from the path - in production only.

This way, everything works:
- Paths resolve on GitHub (→ `/quality/quality-estimation.md`).
- Paths resolve on the website locally (→ `http://localhost:4000/quality-estimation`).
- Paths resolve on website in production (→ `https://machinetranslate.org/quality-estimation`).

So paths should *not* refer to parent directories with `../`.
