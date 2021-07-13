---
description: Parallel data for machine translation
---

# Parallel data

**Parallel data** is a collection of sentences and their corresponding translation. Parallel data is aligned line-by-line. In machine translation, parallel data is also called parallel corpora.

### Goals

Parallel data is necessary to train statistical and neural machine translation engines.

### Challenges

Parallel data is available in most widely spoken languages, but not available in other language pairs.

Parallel data can have errors, like misaligned sentences, bad sentence segmentation, bad encodings, wrong or mixed language. Errors in parallel data are challenging because they affect the quality of the machine translation output. Parallel data errors can be solved via [filtering](customization/filtering.md).

### Public parallel data repositories

- Clarin
- OPUS
- ParaCrawl
