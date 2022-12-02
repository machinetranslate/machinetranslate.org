---
grand_parent: Building and research
parent: Metrics
nav_order: 8
title: BERTScore
description: Evaluation metric using BERT sentence representations
---

**BERTScore** is a metric for automatic evaluation of machine translation that calculates the similarity between a machine translation output and a reference translation using sentence representation.

BERTScore was invented as an improvement on [n-gram](/../concepts/n-gram.md)-based metrics like [BLEU](bleu.md).

> BERTScore addresses two common pitfalls in n-gram-based metrics.
>
> [...] First, such methods often fail to robustly match paraphrases.
>
> [...] Second, n-gram models fail to capture distant dependencies and penalize semantically-critical ordering changes.
>
> For example, given a small window of size two, BLEU will only mildly penalize swapping of cause and effect clauses (e.g. A because B instead of B because A), especially when the arguments A and B are long phrases.
>
> In contrast, contextualized embeddings are trained to effectively capture distant dependencies and ordering.
>
> [*BERTScore: Evaluating Text Generation with BERT*](#resources-and-papers)

The BERTScore metric uses sentence representations from BERT, a deep learning model.

> BERTScore computes precision, recall, and F1 measure.
>
> [*Metric: bert_score*](#resources-and-papers)

### Resources and papers

- [*BERTScore: Evaluating Text Generation with BERT*](https://arxiv.org/pdf/1904.09675.pdf)
- [*Metric: bert_score*](https://huggingface.co/spaces/evaluate-metric/bertscore)
