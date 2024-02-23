---
parent: Customisation
title: Alignment
description: Linking corresponding sentences in the input and output languages
---

**Alignment** is the process of identifying and linking the corresponding sentences in the input and output languages.

Alignment can be used to create [parallel data](/parallel-data).
The aligned parallel corpora are then used to train machine translation models.
The goal is to improve machine translation accuracy through pattern and regularity recognition in data.

## Approaches

- In manual alignment, human translators align corresponding [segmented sentences](/sentence-splitting) in the input and output languages.
- Rule-based approaches use explicit heuristic rules, such as sentence length, word order, or other patterns observed in parallel data.
- Statistical models rely on statistical algorithms that find and analyse relationship patterns in comparable corpora.
The statistical relationships are based on the likelihood of observing alignments in a training corpus.
- With neural approaches, alignment is predicted automatically through [neural networks](/neural-machine-translation#neural-networks) by mapping the input and output sentences into [vectors](/vector).

## Challenges

- Aligning sentences with varying lengths, punctuation, and complex structures can be challenging for alignment algorithms.
- Many words and phrases can have multiple meanings or form idiomatic expressions.
Semantic ambiguity can trigger inaccurate sentence alignments. 
- Typological similarities of languages can result in sentence pairs that share highly similar linguistic properties but have different meanings and translations.
Similarity-based interference can lead to incorrect alignments.
