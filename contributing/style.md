---
nav_order: 1
parent: Contributing
title: Style
description: The Machine Translate style guide
---

Machine Translate was founded as open resources and community for people who want to use machine translation in their work, products or services. They are diverse and busy, so the content should be high-level and understandable.

> **Less is more.**

# 📚 Content

## 📋 Default to Wikipedia style

Default to the Wikipedia's [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) and the [European Commission English Style Guide](https://ec.europa.eu/info/sites/default/files/styleguide_english_dgt_en.pdf) with regard to:

* Content that's neutral, factual and evergreen 🌿
* Titles, capitalization, punctuation and formatting 📖
* Linking to other articles with relative paths ⛓

Default to UK English orthography and to International English vocabulary.


## ♻️ Minimal content

Unlike Wikipedia, the goal is to provide a helpful overview that is easy to read in full and easy to maintain.

Keep pages short, paragraphs short and sentences short and simple.

Add lists for clarity at a glance.

Avoid parentheses, except for defining common abbreviations.

> ... translation management system (TMS) ...


## ❌ No marketing

Do not promote businesses and do not use cliché or meaningless terms.

* _language barriers_
* _multilingual audiences_


## 🙅 Not too academic

Talk straight and make complex topics simple.


## 🈹 Machine translation ready

Machine Translate will be machine translated. Write articles that are ready for machine translation:

- Follow the [Minimal content](#Minimal-content) guidelines.
- Be concise and consistent.
- Use active voice.
- Check spelling.


## 📅 Chronological order

Arrange events, publications, and any information related to time in chronological order.


## 👯 Consistency

Keep consistency with the other articles style.

- _Goals_
- _Challenges_


## 🎤 Machine Translate and machinetranslate.org

Refer to this project and community as _Machine Translate_.


# 🎨 Formatting

## 🔠 Capitalization

In headers, capitalize only the first letter.

> How to contribute


## 🪐 Spacing

❗️ Avoid double spaces and trailing spaces.


## ✒️ Oxford comma

Use the Oxford comma [where appropriate](https://en.wikipedia.org/wiki/Wikipedia:Guidance_on_applying_the_Manual_of_Style#Oxford_comma).


## 👍 Apostrophes and quotation marks

Use curly apostrophes and quotation marks.

> ‘...’

> “...”

> ’


## ⚠️ Acronyms and abbreviations

Only use widely understood acronyms. Expand acronyms they first time they appear in an article.

> Neural machine translation (NMT)

❗️ Do not overuse acronyms. Do not use abbreviations.


## 🧷 Links

Only link **the same** word or phrase once per article.

Avoid **external** links, except for databases, important papers and events.


## ✅ Lists

For list items without a main verb, use initial lowercase and no end punctuation.

```
For list items without verbs:

- item 1
- item 2
- item 3

```

For list items with verbs, use initial uppercase and a period.

```
For list items with verbs:

- Item 1 starts with uppercase and ends with a period.
- Item 2 starts with uppercase and ends with a period.
- Item 3 starts with uppercase and ends with a period.

```

## 👶 File names

When creating a new article, give the file a name that does not exist in Machine Translate.


# 🔨 Markdown

Machine Translate articles are written in [Markdown](https://www.markdownguide.org/cheat-sheet/).

Follow the structure from published Machine Translate articles.


## 📓 Front Matter

Add [Front Matter](https://jekyllrb.com/docs/front-matter/) variables at the beginning of each article.

```
---
parent: Customization
title: Training data
description: Training data for machine translation
---
```

- `parent` is the name of the section.
- `title` is the article header.
- `description` is a phrase that summarizes the content.


## 📰 Headers

The Front Matter `title` will automatically be displayed as an H1.

For sections header, use H3.

```
### Challenges
```

## 📜 Body

Leave an empty line between sub-headers and paragraphs.

Leave an empty line between text and tables.

```
### Schedule

|      |      |
| ---- | ---- |
| 8:00 | **Opening** |
```
