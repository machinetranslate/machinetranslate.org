---
nav_order: 1
parent: Contributing
title: Style
description: The Machine Translate style guide
---

Machine Translate was founded as open resources and community for people who want to use machine translation in their work, products or services. They are diverse and busy, so the content should be high-level and understandable.

> **Less is more.**

# 📚 Content

## Default to Wikipedia style

Default to the Wikipedia's [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) and the [European Commission English Style Guide](https://ec.europa.eu/info/sites/default/files/styleguide_english_dgt_en.pdf) with regard to:

* Content that's neutral, factual and evergreen
* Titles, capitalization, punctuation and formatting
* Linking to other articles with relative paths

Default to UK English orthography and to International English vocabulary.


## Minimal content

Unlike Wikipedia, the goal is to provide a helpful overview that is easy to read in full and easy to maintain.

Keep pages short, paragraphs short and sentences short and simple.

Add lists for clarity at a glance.

Avoid parentheses, except for defining common abbreviations.

> ... translation management system (TMS) ...


## No marketing

Do not promote businesses and do not use cliché or meaningless terms.

* _language barriers_
* _multilingual audiences_


## Not too academic

Talk straight and make complex topics simple.


## Machine Translate and machinetranslate.org

Refer to this project and community as _Machine Translate_.


# 🎨 Formatting

## Capitalization

In headers, capitalize only the first letter.

> How to contribute

## Spacing

Avoid double spaces and trailing spaces.

## Acronyms and abbreviations

Only use widely understood acronyms. Expand acronyms they first time they appear in an article.

> Neural machine translation (NMT)

Do not overuse acronyms. Do not use abbreviations.


## Links

Avoid **external** links, except for databases, important papers and events.

Link anchor texts only the first time they appear in an article.


## File names

When creating a new article, make sure its file name does not already exist.


# 🔨 Markdown

Machine Translate articles are written in [markdown](https://www.markdownguide.org/cheat-sheet/).

Follow the structure from published Machine Translate articles.


## Front matter

Add front matter parameters at the beginning of each article.

```
---
parent: Customization
title: Training data
description: Training data for machine translation
---
```

- **Parent** is the name of the section.
- **Title** is the article header.
- **Description** is a phrase that summarizes the content.


## Headers

The front matter `title` is the article header.

```
---
title: Training data
---
```

Create article sub-headers in H3.

```
### Challenges
```

## Body

Leave an empty line between sub-headers and paragraphs.

Leave an empty line between text and tables.

```
### Schedule

|      |      |
| ---- | ---- |
| 8:00 | **Opening** |
```


## Consistency

Keep consistency with the other articles style.

- _Goals_
- _Challenges_
