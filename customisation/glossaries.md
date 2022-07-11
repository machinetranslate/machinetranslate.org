---
grand_parent: Building and research
parent: Customisation
layout: coming_soon
title: Glossaries
description: Terminology lists for customising and training  machine translation
---
#Glossaries

Multilingual glossaries are lists of terms in one language aligned to their translation in one or more languages. Glossaries can be used to customise machine translation for specific words and phrases.
Glossaries can fix issues related to the translation of:
- terminology
- named entities
- loanwords or do-not-translate items

## Application

Unlike parallel data, glossaries are typically leveraged at translation time, not at training time.
When a glossary term is matched in the source sentence, its translation is enforced in the output.

The insertion of a glossary term in the output happens regardless of the context.
The terms included in the glossary should therefore be unambiguous and context-independent, as in the following examples:
- en: `Respiratory syndrome`
- en: `Balance sheet`
- en: `Paraffin`

Ambiguous terms can have a negative impact on the output:
- en: `Spread`
- en: `Cookies`
- en: `Surface treatment`

##Term matching and insertion

Some machine translation systems can use glossaries to improve their output.
Machine translation systems differ in how they match and insert glossary terms.s

Strict exact term matching has many limitations since terms can have varying forms. With some machine translation systems, term matching can handle common variants.
- Morphology inflections
- Casing forms
- Spelling forms

In some machine translation systems, term insertion can handle common variants, according to the context.
- Morphological agreement
- Casing

## Glossary term forms

With strict exact matching and insertion, more variants need to be listed in the glossary.
- Morphology
  - Singular and plural forms
  - Masculine and feminine forms
  - Verb inflections
- Ortography
  - Casing (uppercased, lowercased, capitalised, not capitalised)

If the term is matched regardless of its form and is inflected so that it agrees with the rest of the items in the target sentence, it is possible to include in the glossary only the dictionary form of each term.

## File formats

Machine translation systems support a few glossary file formats.
- TBX (TermBase eXchange)
- CSV
- TSV
- XLSX (spreadsheets)
