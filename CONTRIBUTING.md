---
nav_order: 400
has_children: true
title: Contributing
description: How to contribute to Machine Translate
permalink: /contributing
seo:
  type: HowTo
  name: Contributing
  step:
    type: HowToStep
    name: Read the roadmap
    position: 1
  step:
    type: HowToStep
    name: Create and edit articles
    position: 2
  step:
    type: HowToStep
    name: Review proposed changes
    position: 3
  step:
    type: HowToStep
    name: Request articles
    position: 4
  step:
    type: HowToStep
    name: Contribute to infrastructure
    position: 5
---

Machine Translate is **created and edited by [contributors like you!](contributing/contributors.md)**.
It is **open-source** and lives [**on GitHub**](https://github.com/machinetranslate/machinetranslate.org).

We recommend reading the [**roadmap**](/roadmap.md) and [**style guide**](contributing/style.md) before you start contributing.

### Creating and editing articles

To create or edit an article, [**create**](https://github.com/machinetranslate/machinetranslate.org/new/master) or [**edit**](https://github.com/machinetranslate/machinetranslate.org) and send us a [pull request](https://github.com/machinetranslate/machinetranslate.org/pulls?q=is%3Apr).

> See GitHub’s article [*Creating a pull request*](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request#creating-the-pull-request) for more.

Many articles are automatically generated from [data files](https://github.com/machinetranslate/machinetranslate.org/tree/master/_data).

> #### How to add a language
> To add a new language:
> - Add the language to [languages.yml](https://github.com/machinetranslate/machinetranslate.org/blob/master/_data/languages.yml).
> - Add the language family to [language-families.yml](https://github.com/machinetranslate/machinetranslate.org/blob/master/_data/language-families.yml), if it does not exist yet.
>
> The articles of the APIs that support that language will automatically be updated the next time that [generate.py](https://github.com/machinetranslate/machinetranslate.org/blob/master/generate.py) is run.

### Reviewing proposed changes

You can also contribute by reviewing other contributors' [open pull requests](https://github.com/machinetranslate/machinetranslate.org/pulls?q=is%3Aopen+is%3Apr).

> See GitHub’s article [*Commenting on a pull request*](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request ) for more.

### Requesting articles

To request a topic, create a new [**issue**](https://github.com/machinetranslate/machinetranslate.org/issues).

> See GitHub’s article [*Creating an issue*](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue#creating-an-issue-from-a-repository) for more.

---

### Contributing to infrastructure

To contribute technical work not content, start by reading [README.md](https://github.com/machinetranslate/machinetranslate.org/blob/master/README.md).
