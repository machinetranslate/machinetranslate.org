---
description: Parallel data for machine translation
---

# Parallel data

**Parallel data** or **parallel corpora** are datasets of **translation pairs** - sentences and their translations. They are used to train and test machine translation models.

| Original | Translation |
| ----------- | ----------- |
| File | Archivo |

Parallel datasets can include translations for one or more language pairs, and be directioned or directionless.

Parallel data can be created by crawling and aligned monolingual test, and by [back-translation](customization/back-translation.md) or [back-copying](customization/back-translation.md).

### Goals

Parallel data is necessary to train statistical and neural machine translation engines.

### Challenges

Parallel data is available in most widely spoken languages, but not available in other language pairs.

Parallel data can have errors, like misaligned sentences, bad sentence segmentation, bad encodings, wrong or mixed language. Errors in parallel data are challenging because they affect the quality of the machine translation output. Parallel data errors can be solved via [filtering](customization/filtering.md).

### Public parallel data repositories

- Clarin
- OPUS
- ParaCrawl
