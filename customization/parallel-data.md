---
parent: Customization
title: Parallel data
description: Parallel data for training machine translation
---

# Parallel data

**Parallel data** or **parallel corpora** are datasets of **translation pairs** - sentences and their translations. They are used to train and test machine translation models.

| Original | Translation |
| ----------- | ----------- |
| File | Archivo |

Parallel datasets can include translations for one or more language pairs, and be directioned or directionless.

### Parallel data creation

Parallel datasets can be created manually, automatically, or created synthetically from monolingual data.
- Human translation or human [post-editing](/workflows/post-editing)
- [Crawling](/research/crawling), [alignment](/research/alignment) and [filtering](/customization/filtering)
- [Back-translation](/customization/back-translation.md)
- [Back-copying](/customization/back-translation.md)

### Goals

Parallel data is used to train statistical and neural machine translation engines.

### Challenges

Parallel data is available for most widely written language pairs, but not available for other language pairs.

Parallel data can have errors, like misaligned sentences, bad sentence segmentation, bad encodings, wrong or mixed language. Errors in parallel data are challenging because they affect the quality of the machine translation output. Parallel data errors can be solved via [filtering](filtering.md).

### Public parallel data

| Name | Type |
| ---- | ---- |
| CCAligned | Data repository |
| CCMatrix | Data repository |
| Clarin | Data repository |
| Europarl | Data set |
| FLORES | Data set |
| Hansard | Data set |
| JESC | Data set |
| Mozilla | Data repository |
| OpenSubtitles | Data repository |
| ParaCrawl | Data repository |
| VoxPopuli | Data set |
| WikiMatrix | Data repository |
| WikiTitles | Data repository |
