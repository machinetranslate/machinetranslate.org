---
parent: Customization
title: Filtering
description: Filtering training data for machine translation
---

**Filtering** for machine translation is the process of cleaning [parallel data](parallel-data.md) for training a machine translation system.

Parallel data can be filtered manually or automatically.

To filter parallel data, risky translations and obvious noise are either dropped or fixed.

Risky translations include, for example:

* Creative human translations
* Translations that are structured differently than the original

Obvious noise includes, for example:

* Sentences with mismatched URLs, names, or numbers
* Translated sentences that are equal to their original

### Tools

* ModelFront
* Zipporah
* Bicleaner
* LASER

### Techniques

* Normalization
* [Tokenization](/customization/tokenization.md)
* Removing duplicate segments
* Removing non-alphabetical symbols
* Removing irrelevant languages
* Spelling out or collapsing acronyms
* Replacing named entities with placeholders
* Matching the original and the translated sentences punctuation
* Fixing typos and spelling mistakes
