---
grand_parent: Building and research
parent: Metrics
nav_order: 6
title: NIST
description: National Institute of Standards and Technology
---

**NIST** (**National Institute of Standards and Technology**)  is a metric for automatic evaluation of machine translation that calculates the similarity between a machine translation output and a reference translation using [n-grams](/../concepts/n-gram.md) precision.

NIST is an adaptation of [BLEU](bleu.md).

Compared to BLEU, NIST gives more importance to the less frequent n-grams.

> The NIST metric is derived from the BLEU evaluation criterion but differs in one fundamental aspect: instead of n-gram precision, the information gain from each n-gram is taken into account.


### See more:

- [aclanthology.org/www.mt-archive.info/HLT-2002-Doddington.pdf](https://aclanthology.org/www.mt-archive.info/HLT-2002-Doddington.pdf)
