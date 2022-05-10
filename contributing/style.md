---
nav_order: 1
parent: Contributing
title: Style
description: The Machine Translate style guide
---

Machine Translate was founded as open resources and community for people who want to use machine translation in their work, products or services. They are diverse and busy, so the content should be high-level and understandable.

> **Less is more.**

{% include collapsible_toc.html %}

# 📚 Content

## Default to Wikipedia style

Default to the Wikipedia’s [Manual of Style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) and the [European Commission English Style Guide](https://ec.europa.eu/info/sites/default/files/styleguide_english_dgt_en.pdf):

* Create content that is neutral, factual and evergreen.
* Follow their guidelines in titles, capitalisation, punctuation, and formatting.
* Link to other articles with relative paths.

Default to UK English orthography and to International English vocabulary.


## Minimal content

Unlike Wikipedia, the goal is to provide a helpful overview that is easy to read in full and easy to maintain.

Keep pages short, paragraphs short and sentences short and simple.

Add lists for clarity at a glance.

Avoid parentheses, except for defining common abbreviations.

> ... translation management system (TMS) ...


## Consistency

Use sister articles as reference and keep consistency with their structure.  Similar articles should have similar sections and focus on the same kind of information.


## No marketing

Do not promote businesses.


## No empty phrases

Do not use cliché or meaningless terms.

* _language barriers_
* _multilingual audiences_


## No prescriptions

Write about facts that are always true.

* _Post-editing effort ~~may be~~ is..._


## Not too academic

Talk straight and make complex topics simple.


## Machine translation ready

Machine Translate will be machine translated. Write articles that are ready for machine translation:

- Follow the [Minimal content](#minimal-content) guidelines.
- Be concise and consistent.
- Use active voice.
- Check spelling.
- Use nouns instead of pronouns.

> Tags format, structure and annotate texts. ~~They~~ Tags can also be used as placeholders.

## Chronological order

Arrange events, publications, and any information related to time in chronological order.

## Names list

In lists, separate names with commas. Do not add “and” before the last name.

> Philipp Koehn, Franz Josef Och, Daniel Marcu


## Machine Translate and machinetranslate.org

Refer to this project and community as _Machine Translate_.


# 🎨 Formatting

## Capitalisation

In headers, capitalise only the first letter.

> How to contribute


## Spacing

Avoid trailing spaces and double spaces inside sentences.

Separate sentences with two spaces.


## Dates

Put dates before months.  Omit the leading `0` in single-digit dates.

> 2 June, 2019


## Times

Include the leading `0` in single-digit hours.

> 09:00

Use `-` to separate time ranges.

> 09:00 - 09:30


## Oxford comma

Use the Oxford comma [where appropriate](https://en.wikipedia.org/wiki/Wikipedia:Guidance_on_applying_the_Manual_of_Style#Oxford_comma).


## Apostrophes and quotation marks

Use curly apostrophes and quotation marks.

> ‘...’

> “...”

> ’


## Acronyms and abbreviations

Only use widely understood acronyms. Expand acronyms the first time they appear in an article.

> Neural machine translation (NMT)

Do not overuse acronyms.

Do not use abbreviations.  Do not use punctuation marks as abbreviations.

> ~~USD/EUR~~ USD or EUR


## Links

Only link **the same** word or phrase once per article.

Avoid **external** links, except for databases, important papers and events.


## Lists

Introduce lists with full sentences.

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

## File names

When creating a new article, give the file a name that does not exist in Machine Translate.


# 🔨 Markdown

Machine Translate articles are written in [Markdown](https://www.markdownguide.org/cheat-sheet).

Follow the structure from published Machine Translate articles.


## Front Matter

Add [Front Matter](https://jekyllrb.com/docs/front-matter) variables at the beginning of each article.

```
---
parent: Customisation
title: Training data
description: Training data for machine translation
---
```

- `parent` is the name of the section.
- `title` is the article header.
- `description` is a phrase that summarizes the content.


## Headers

The Front Matter `title` will automatically be displayed as an H1.

For sections header, use H3.

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

## Links

For articles in the **same directory**, use a **relative** path.

```
She researches quality estimation with [Kevin Johnson](kevin-johnson.md) at Microsoft.
```

For articles in any **other directory**, use an **absolute** path.

```
She researches [quality estimation](quality/quality-estimation.md) with Kevin Johnson at Microsoft.
```

For a specific **section** of an article, use the **fragment identifier**.

```
She researches quality estimation with Kevin Johnson at [Microsoft](industry/companies.md#microsoft).
```

Avoid trailing slashes at the end of links.

> jekyllrb.com/docs/front-matter~~/~~


## Mathematical notation

To render short mathematical formulas, like <img src="https://render.githubusercontent.com/render/math?math=p(t_i|s_{1\ldots |s|}, t_{1\ldots (i-1)})">, use [LaTeX](https://www.latex-project.org/about/) notation and insert the LaTeX code after `=` in the below URL.

`<img src="https://render.githubusercontent.com/render/math?math=[LaTeX Code]">`


Include the complete URL to add the mathematical formula in the article.

```
<img src="https://render.githubusercontent.com/render/math?math=p(t_i|s_{1\ldots |s|}, t_{1\ldots (i-1)})">
```
