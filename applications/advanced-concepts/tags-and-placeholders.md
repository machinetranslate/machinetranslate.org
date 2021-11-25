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


English original:  
`A <b>red</b> car`

Expected translation into Spanish:  
`Un auto <b>rojo</b>`

Translation into Spanish with misplaced tag:  
`Un <b>auto</b> rojo`

Translation into Spanish with a corrupted tag:  
`Un auto b rojo b`


## Placeholders

Placeholders are variables for dynamic content.
For machine translation, placeholders are challenging because their content can be ambiguous.
Like tags, placeholders can also be misplaced, corrupted or dropped in the output.

Original in English:  
`There are {number} pages in the book.`

Expected translation into Spanish:  
`Hay {number} páginas en el libro.`

Translation into Spanish with corrupted placeholder:  
`Hay { páginas } páginas en el libro.`
