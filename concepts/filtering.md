---
parent: Customisation
title: Filtering
description: Filtering training data for machine translation
featured: true
---

**Filtering** for machine translation is the process of cleaning [parallel data](/parallel-data) for training a machine translation system.

Parallel data can be filtered manually or automatically.

To filter parallel data, translation pairs with obvious noise and risky translations are dropped.

Translations pairs are also dropped if they have other obvious issues:

* Translations to the wrong language
* Sentence pairs with mismatched URLs, names, or numbers
* Sentence pairs with mismatched tags
* Sentence pairs with mismatched length
* Translations with broken encoding or invalid characters

Some sentence pairs have issues that are more difficult to filter out.

* Creative human translations
* Translations that are structured differently than the original
* Translations that are equal to the original
* Translations from a third language
* Very short input

Preprocessing is often normalisation.
* Decoding or encoding
* Invalid characters
* Leading or trailing whitespace
* Alternative whitespace characters
* Alternative punctuation characters

Filtering and preprocessing can hurt translation quality, by removing or changing useful data.

### Tools

* ModelFront
* Zipporah
* Bicleaner
* LASER

### Techniques

* Normalisation
* [Tokenisation](/tokenisation)
* Removing duplicate segments
* Removing non-alphabetical symbols
* Removing irrelevant languages
* Spelling out or collapsing acronyms
* Replacing named entities with placeholders
* Matching the original and the translated sentences punctuation
* Fixing typos and spelling mistakes
