---
parent: Customisation
title: Back-translation
description: Back-translating or back-copying target language sentences to augment parallel data
---

**Back-translation** is the process of translating the monolingual data in the target language into the source language and then back into the target language.
The goal is to generate synthetic [parallel data](/customisation/parallel-data.md) that can be used to train machine translation systems.

**Back-copying** is a similar technique to back-translation.
The process involves using an existing translation to create a new parallel sentence pair in the opposite direction.

### Challenges

Back-translation is challenging for language pairs with significantly different syntactic and semantic features, resulting in low-quality parallel data.

Back-copying generates parallel data that is identical in the source and target languages.
The lack of diversity can result in a machine translation system that is overly reliant on the [training data](/customisation/training-data.md) and performs poorly on unseen data.
