---
nav_order: 30
parent: Approaches
has_children: true
title: Neural machine translation
description: Deep learning approaches to machine translation
---

**Neural machine translation** (NMT) is a machine translation approach based on machine learning that uses large neural networks to predict the likelihood of correct translations. Like [statistical machine translation](statistical-machine-translation.md), neural machine translation is data-driven.

### Neural networks

Neural networks use [training data](../customization/training-data.md) to create [vectors](../concepts/vector.md) for every word and its relations, called word embeddings. Words with similar meaning cluster together and words with more than one meaning appear simultaneously in different clusters.

**Cluster<sub>1</sub>**:
- **Bank**
- Lake
- River
- Stream
- Terrain

**Cluster<sub>2</sub>**:
- Money
- Finance
- Credit
- **Bank**
- Banking

Neural networks use cluster information to disambiguate the meaning of input words and model the most relevant translations.

### Sequence model

In general, neural machine translation can be seen as a sequence-to-sequence task. Given an input sequence, the system predicts and generates an output sequence. The sequence model arranges a sentence order by calculating the probability of the sequence of words.

### Encoder/decoder framework

Neural machine translation architecture consists of an encoder and a decoder.

The encoder analyzes the input sequence words and their relations. The result is the representation of the sentence, called context vector. The context vector summarizes the entire input sequence into a single fixed-length vector.

The decoder takes that sequence representation and produces the translation.

### Attention mechanism

Single fixed-length vectors are too limited to cram all the information from long sentences.

A solution to this problem is to employ an attention mechanism. An attention mechanism focuses on the input sentence areas that are relevant instead of looking at the complete input sentence. The attention mechanism also learns the alignment between the relevant information.
