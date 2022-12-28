---
grand_parent: Building and research
parent: Metrics
nav_order: 4
title: COMET
description: Evaluation metric using embeddings
---

**COMET** (**Crosslingual Optimized Metric for Evaluation of Translation**) is a metric for automatic evaluation of machine translation that calculates the similarity between a machine translation output and a reference translation using token or sentence embeddings.

It is based on similarity of vector representations.

> Traditionally only QE models have made use of the source input, whereas MT evaluation metrics rely instead on the reference translation. [...], we show that using a multilingual embedding space allows us to leverage information from all three inputs and demonstrate the value added by the source as input to our MT evaluation models.
>
> [*COMET: A Neural Framework for MT Evaluation*](#resources-and-papers)

Unlike [BERTScore](bertscore.md), COMET is trained on predicting different types of human judgements in the form of post-editing effort, direct assessment or translation error analysis.

### Resources

- [*COMET: A Neural Framework for MT Evaluation*](https://aclanthology.org/2020.emnlp-main.213.pdf)
