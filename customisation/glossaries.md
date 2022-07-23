---
grand_parent: Building and research
parent: Customisation
layout: coming_soon
title: Glossaries
description: Terminology lists for customising machine translation
---
# Glossaries

Multilingual glossaries are lists of terms in one language aligned to their translation in one or more languages.
Glossaries can be used to customise machine translation for specific words and phrases.
- terminology
- named entities
- "do-not-translate" words or phrases

## Application

Unlike parallel data, glossaries are typically applied at translation time, not at training time.

When a glossary term is matched in the source sentence, its translation is inserted in the output.

The insertion of a glossary term in the output happens regardless of the context.

The terms included in the glossary should therefore be unambiguous and context-independent, as in the following examples:
- en: `Respiratory syndrome`
- en: `Balance sheet`
- en: `Paraffin`

Ambiguous terms can have a negative impact on the output:
- en: `Spread`
- en: `Cookies`
- en: `Surface treatment`

## Term matching and insertion

Machine translation systems differ in how they match and insert glossary terms.

Strict exact term matching and insertion has many problems.
With strict exact matching and insertion, many variants may need to be listed in the glossary.
Even then, the correct variant may not be inserted.

With some machine translation systems, term matching and insertion can handle common variants.
- Spelling variants
- Uppercase and lowercase variants
- Morphological inflections

## File formats

Machine translation systems support a few glossary file formats.
- TBX (TermBase eXchange)
- TMX
- CSV
- TSV
- XLSX (spreadsheets)
