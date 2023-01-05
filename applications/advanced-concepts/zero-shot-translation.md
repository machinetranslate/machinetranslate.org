---
parent: Building and research
title: Zero-shot translation
description: Machine translation without parallel training data
---

**Zero-shot machine translation** is translation without parallel data between the source and target languages.
Zero-shot translation is desirable because it can be too costly to create training data for each language pair.
However, zero-shot models are typically lower quality than models trained from parallel data.
The term zero-shot is a reference to [zero-shot learning](https://en.wikipedia.org/wiki/Zero-shot_learning).

Zero-shot machine translation is an active area of research.

## Approaches

- Bridging: If a language pair `(source, target)` is desired, this approach translates twice: `(source, bridge)`, then `(bridge, target)`. The `bridge` language is also called a pivot language. English is a common choice for the pivot because many languages have training data with English.
- Multilingual [neural machine translation](/approaches/neural-machine-translation.md) (MNMT): This approach learns a single model for all language pairs. The target language is an input to the model. This approach can produce translations between languages that both have parallel data, but not necessarily parallel data with each other. 
- Transfer learning: These approaches connect an encoder for the source language to a decoder for the target language. Algorithms are developed to align the latent representations of encoders and decoders across languages.

