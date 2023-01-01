---
parent: Building and research
title: Zero-shot translation
description: Machine translation without parallel training data
---

**Zero-shot machine translation** is machine translation that is trained without parallel data between the source and target languages.
Zero-shot translation is desireable because it can be prohibitively time-consuming or costly to build a training corpus of parallel texts to build a normal translation model for each pair of languages.

Zero-shot machine translation is an active area of research, and models are typically lower quality than supervised translation models.

## Approaches

- Multilingual machine translation: Rather than learn one model per language pair, this approach learns a single model for all language pairs. The target langauge is an input to the model. This approach can produce translations between languages that both have parallel data, but not necessarily parallel data with each other.
- Pivoting/bridging: If a language pair (a, c) is desired, this approach translates twice: (a, b), then (b, c) where b is called the pivot or bridge language. English is a common choice for the pivot because there's often parallel data with English.
- Denoising autoencoders: This approach trains two denoising autoencoders on monolingual data, one for the source language and one for the target language. Then the encoder from the source language is connected to the decoder for the target language in the hope that the latent representations of the two are similar.

## Related

- Cross-lingual fine-tuning
- Adversarial training

## TODO

- Clarify the data needs of the approaches: MNMT and pivoting still require some parallel data of the language, they just don't need the (source, target) pair
- Introduce the term unsupervised MT for denoising AEs -- there's an issue open for a page on this
- It'd be nice to give a sense of the quality of zero-shot compared to supervised approaches
- It'd be nice to answer a question like "Should I use zero-shot MT?" or offer some guidance on when to use which type of approach, though that may be better suited for the "How to get machine translation for your language" issue
