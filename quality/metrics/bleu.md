---
grand_parent: Building and research
parent: Metrics
nav_order: 2
title: BLEU
description: Evaluation metric based on n-gram precision
---

**BLEU** (**BiLingual Evaluation Understudy**) is a metric for automatic evaluation of machine translation that calculates the similarity between a machine translation output and a reference translation using [n-gram](/../concepts/n-gram.md) precision.

Its basic unit of evaluation is the sentence.

> The closer a machine translation is to a professional human translation, the better it is.
>
> [*BLEU: a Method for Automatic Evaluation of Machine Translation*](#resources-and-papers)

BLEU is the standard metric for machine translation evaluation.

BLEU compares machine translation output to a single reference translation.

BLEU treats all n-grams equally.

Because BLEU is not an exactly defined metric, BLEU scores are not comparable.
So researchers have created variants that are more concretely defined.
Here are some of the most well-known variants of BLEU:

- sacreBLEU
- BLEUrt
- M-BLEU

*Note: The list is incomplete.*

### Resources and papers

- [*BLEU: a Method for Automatic Evaluation of Machine Translation*](https://aclanthology.org/P02-1040.pdf)
