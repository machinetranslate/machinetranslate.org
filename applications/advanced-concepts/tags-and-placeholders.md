---
description: Tags and placeholders in machine translation
---

# Tags and placeholders

**Tags** and **placeholders** are pieces of non-translatable code inside the input text.

## Tags

Tags format, structure and annotate texts, and can also be used as placeholders. Tags are usually XML, for example HTML.

There are two approaches for working with tagged inputs:

1. Tags are kept in the training data and at runtime. This can affect the quality of the (non-tagged) machine translation output.
2. Tags are removed in the training data and at runtime, and reinserted after translation.

With either approach, tags may be misplaced, corrupted or dropped in the output.


#### Example

Original in English: \<service\> account

Expected translation: la cuenta de \<service\>

Translation with misplaced tag: \<service\> cuenta

## Placeholders

Placeholders are variables for dynamic content.
For machine translation, placeholders are challenging because their content can be ambiguous.
Like tags, placeholders can also be misplaced, corrupted or dropped in the output.

#### Example

Original in English: There are {number} pages in the book.

Expected translation: Hay {pages} páginas en el libro.

Translation with corrupted placeholder: Hay { páginas } páginas en el libro.
