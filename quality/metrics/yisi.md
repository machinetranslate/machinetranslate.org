---
grand_parent: Building and research
parent: Metrics
nav_order: 5
title: YiSi
description: Evaluation metric using sentence representation
---

**YiSi** is a metric for automatic evaluation of machine translation that calculates the similarity between a machine translation output and a reference translation using sentence representation.

The term YiSi comes from the Cantonese word 意思, which means ‘meaning’.

> YiSi is a unified semantic MT quality evaluation and estimation metric for languages with different levels of available resources.
>
> [*YiSi - A unified semantic MT quality evaluation and estimation metric for languages with different levels of available resources*](#resources-and-papers)

### Variants

YiSi offers different variants depending on the resources available for the evaluation.

| YiSi-0 | YiSi-1 | YiSi-2 |
| --- | --- | --- |
| Can be deployed to any language pair | Requires an embedding model | Requires a crosslingual embedding model |
| Measures lexical similarity via longest common character substring | Aggregates the similarity in meaning of the embeddings | Optionally requires a semantic role labeler in both input and output language |
| Compares machine translation output and human reference | Can incorporate shallow semantic structures | Evaluates the crosslingual semantic similarity using bilingual embeddings |
| | | Can also estimate quality without any reference |


### Resources and papers

- [*YiSi - A unified semantic MT quality evaluation and estimation metric for languages with different levels of available resources*](https://aclanthology.org/W19-5358.pdf)
- [github.com/chikiulo/yisi](https://github.com/chikiulo/yisi)
