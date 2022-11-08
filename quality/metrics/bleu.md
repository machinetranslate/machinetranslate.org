---
grand_parent: Building and research
parent: Metrics
nav_order: 1
title: BLEU
description: BiLingual Evaluation Understudy
---

**BLEU** (BiLingual Evaluation Understudy) is the standard metric for machine translation evaluation.

> The closer a machine translation is to a professional human translation, the better it is.

BLEU compares machine translation output to a single reference translation.
BLEU is an [n-gram](/../concepts/n-gram.md) word-based metric.

BLEU is based on translation precision.
Its basic unit of evaluation is the sentence.

BLEU treats all n-grams equally.

### Flavours

- sacreBLEU
- BLEUrt
- M-BLEU

*Note: The list is incomplete.*

### See more:

- [Metrics](/../resources/publications#metrics)
