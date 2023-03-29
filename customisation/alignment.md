---
parent: Customisation
title: Alignment
description: Linking corresponding units in the source and target languages
---

**Alignment** is the process of identifying and linking the corresponding text units in the source and target languages.
Data sets can be aligned at the word, phrase, or sentence level.

Alignment can be used to create [parallel data](/customisation/parallel-data.md).
The aligned parallel corpora are then used to train machine translation models.
The goal is to help the machine translation system accurately translate text from one language to another by recognising patterns and regularities in the data. 

#### Example

Sentences are [split](/concepts/sentence-splitting.md) into smaller [tokens](/concepts/token.md).

English: `The` `book` `is` `on` `the` `table` `.`

German: `Das` `Buch` `liegt` `auf` `dem` `Tisch` `.`

By identifying the corresponding words, such as `book` and `Buch` or `table` and `Tisch`, the two example sentences are aligned and used as [training data](/customisation/training-data.md) for the machine translation system.

### Approaches

Machine translation systems use various alignment approaches to link two data sets at different granularity levels.

- In manual alignment, bilingual human translators align corresponding text [segments](/concepts/segment.md) in the source and target languages.
- [Rule-based machine translation](/approaches/rule-based-machine-translation.md) uses linguistic rules and patterns to align words and phrases in two languages.
- The [statistical machine translation](/approaches/statistical-machine-translation.md) models rely on statistical algorithms that find relationships between words and phrases in the source and target languages.
The statistical relationships are based on the likelihood of observing alignments in a training corpus.
- In [neural machine translation](/approaches/neural-machine-translation.md), alignment is learned automatically through [neural networks](/approaches/neural-machine-translation.md#neural-networks).
The neural models can be based on various encoder-decoder architectures, such as convolutional neural networks (CNNs), recurrent neural networks (RNNs), or [transformer](/approaches/transformers.md) models.

### Challenges

- The word order, sentence structure, and punctuation can differ significantly between languages, making it challenging to align sentences at the word or phrase level.
- Many words and phrases can have multiple meanings or form idiomatic expressions.
Semantic ambiguity can result in inaccurate sentence alignments. 
- Out-of-vocabulary (OOV) words that are not present in the machine translation system [vocabulary](/concepts/vocabulary.md) can result in errors in the translation.
