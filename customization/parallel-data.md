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
- Human translation
- Human [post-editing](/workflows/post-editing.md)
- [Crawling](/research/crawling.md)
- [Alignment](/research/alignment.md)

### Goals

Parallel data is used to train statistical and neural machine translation engines.

### Challenges

Parallel data is available for most widely written language pairs, but not available for other language pairs.

Parallel data can have errors, like misaligned sentences, bad sentence segmentation, bad encodings, wrong or mixed language. Errors in parallel data are challenging because they affect the quality of the machine translation output. Parallel data errors can be solved via [filtering](filtering.md).

### Public parallel data

| Name | Type |
| ---- | ---- |
| [CCAligned](https://opus.nlpl.eu/CCAligned.php) | Data repository |
| [CCMatrix](https://github.com/facebookresearch/LASER/tree/main/tasks/CCMatrix) | Data repository |
| [Clarin](https://www.clarin.eu/resource-families/parallel-corpora) | Data repository |
| [Europarl](https://www.statmt.org/europarl/) | Data set |
| [FLORES](https://github.com/facebookresearch/flores) | Data set |
| [Hansard](https://catalog.ldc.upenn.edu/LDC95T20) | Data set |
| [JESC](https://nlp.stanford.edu/projects/jesc/) | Data set |
| [Mozilla Common Voice](https://commonvoice.mozilla.org/en/datasets) | Data repository |
| [OpenSubtitles](https://opus.nlpl.eu/OpenSubtitles-v2018.php) | Data repository |
| [ParaCrawl](https://paracrawl.eu/) | Data repository |
| [VoxPopuli](https://github.com/facebookresearch/voxpopuli) | Data set |
| [WikiMatrix](https://github.com/facebookresearch/LASER/tree/main/tasks/WikiMatrix) | Data repository |
| [WikiTitles](https://huggingface.co/datasets/wmt/wikititles) | Data set |
