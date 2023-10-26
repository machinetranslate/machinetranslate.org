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

- Multilingual [neural machine translation](../../building-and-research/approaches/neural-machine-translation.md) (MNMT): This approach learns a single model for all language pairs. The target language is an input to the model. This approach can produce translations between languages that both have parallel data, but not necessarily parallel data with each other. As of 2022, [Google Translate uses MNMT](https://ai.googleblog.com/2022/05/24-new-languages-google-translate.html).
- Stitching together encoders and decoders
    - When training models for many language pairs, it's possible to ensure that the latent representations are similar across languages, then connect the appropriate encoder and decoder for the desired language pair.
    - Unsupervised methods learn encoders and decoders as denoising autoencoders, making an effort to ensure that the latent representations are similar across languages, then connect the appropriate encoder and decoder for the desired language pair.

## See also

- [Bridging](bridging.md): Bridging is also commonly used to translate between languages without parallel data.
