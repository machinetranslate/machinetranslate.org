---
grand_parent: Building and research
parent: Metrics
nav_order: 4
title: YiSi
description: Crosslingual Optimized Metric for Evaluation of Translation
---

**YiSi** is computes the similarity in meaning of the machine translation output with the input text and the reference translation.
The term YiSi comes from the Cantonese word 意思, which means ‘meaning’.

> YiSi is a unified semantic MT quality evaluation and estimation metric for languages with different levels of available resources.

### Variants

YiSi offers different flavours depending on the resources available for the evaluation.

| YiSi-0 | YiSi-1 | YiSi-2 |
| --- | --- | --- |
| Can be deployed to any language pair | Requires an embedding model | Requires a crosslingual embedding model |
| Measures lexical similarity via longest common character substring | Aggregates the similarity in meaning of the embeddings | Optionally requires a semantic role labeler in both input and output language |
| Compares machine translation output and human reference | Can incorporate shallow semantic structures | Evaluates the crosslingual semantic similarity using bilingual embeddings |
| | | Can also estimate quality without any reference |


### References

- [github.com/chikiulo/yisi](https://github.com/chikiulo/yisi)
- [aclanthology.org/W19-5358.pdf](https://aclanthology.org/W19-5358.pdf)
