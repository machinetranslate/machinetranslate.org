---
grand_parent: Building and research
parent: Customisation
title: Language identification
description: Identifying the language of a text
---

**Language identification** tools identify the language of an unknown text.
In machine translation, language identification tools are used in building monolingual [training data](/customisation/training-data.md) from large collections of unidentified texts such as webpages.
Language identification tools are also used to automatically identify the source language in many machine translation systems when the source language is unspecified.

## Challenges

- Similar languages may be mistaken for one another, for example Dutch and Afrikaans.
- Language identification is more challenging on short pieces of text.
- If a particular [locale](/applications/advanced-concepts/locale.md) is not supported in the language identification tool, it may be misclassified as another, similar locale. For example, if a language identification tool does not support Serbian with the Cyrillic script, it may be misclassified as Macedonian.
