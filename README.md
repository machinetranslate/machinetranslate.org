

*This README is for making changes to machinetranslate.org infrastructure, not Machine Translate content.  The Machine Translate landing page served at [https://machinetranslate.org](https://machinetranslate.org) is **[index.md](index.md)**.*

### Infrastructure

The machinetranslate.org technology stack:
- Website: Jekyll
- CDN: GitHub Pages
- DNS: Cloudflare

### Running Jekyll locally

Follow the [Jekyll Quickstart Instructions](https://jekyllrb.com/docs/#instructions):

> 1. Install all [prerequisites]({{ '/docs/installation/' | relative_url }}).
> 2. Install the jekyll and bundler [gems]({{ '/docs/ruby-101/#gems' | relative_url }}).
> ```sh
> gem install jekyll bundler
> ```
> ...
> ```
> 5. Build the site and make it available on a local server.
> ```sh
> bundle exec jekyll serve
> ```
> 6. Browse to [http://localhost:4000](http://localhost:4000){:target="_blank"}

### Paths

This repository has a directory structure, but on the website the page paths are flat.

> GitHub repository: `/quality/quality-estimation.md`
> machinetranslate.org: `/quality-estimation`

How it works:
- Jekyll removes the file extension (`.md`).
- A Cloudflare Page Rule is configured to remove the directory from the path.
- In the soure content on GitHub, relative paths are used.
- Relative paths resolve on GitHub and on the website.
