---
grand_parent: Building and research
parent: Metrics
nav_order: 3
title: METEOR
description: Metric for Evaluation of Translation with Explicit ORdering
---

**METEOR** (**Metric for Evaluation of Translation with Explicit ORdering**)  is a metric for automatic evaluation of machine translation that calculates the similarity between a machine translation output and a reference translation using [n-grams](/../concepts/n-gram.md).

> Meteor evaluates a translation by computing a score based on explicit word-to-word matches between the translation and a given reference translation.
>
> [*METEOR: An Automatic Metric for MT Evaluation with Improved Correlation with Human Judgments*](#resources-and-papers)

Apart from exact word matching, METEOR adds matching for synonyms and simple morphological variants of a word.

METEOR takes into account both the precision and recall while evaluating a match.

### Variants

- METEOR-NEXT

*Note: The list is incomplete.*

### Resources and papers

- [*METEOR: An Automatic Metric for MT Evaluation with Improved Correlation with Human Judgments*](https://www.cs.cmu.edu/~alavie/METEOR/pdf/Banerjee-Lavie-2005-METEOR.pdf)
