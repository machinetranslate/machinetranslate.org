---
grand_parent: Building and research
parent: Metrics
nav_order: 7
title: BERTScore
description:
---

The **BERTScore** metric calculates the similarity in meaning between the machine translation output and a reference.
BERTScore uses contextual embeddings.

> BERTScore addresses two common pitfalls in n-gram-based metrics. [...] First, such methods often fail to robustly match paraphrases. [...] Second, n-gram models fail to capture distant dependencies and penalize semantically-critical ordering changes For example, given a small window of size two, BLEU will only mildly penalize swapping of cause and effect clauses (e.g. A because B instead of B because A), especially when the arguments A and B are long phrases. In contrast, contextualized embeddings are trained to effectively capture distant dependencies and ordering.

The BERTScore metric uses BERT sentence representation.
BERTScore computes precision, recall, and F1 measure.

### See more:

- [Metrics](/../resources/publications#metrics)
