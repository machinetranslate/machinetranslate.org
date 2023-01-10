---
grand_parent: Building and research
parent: Customisation
title: Language identification
description: Identifying the language of a text
---

**Language identification** is the process of identifying the language of a text.
Language identification tools output a [locale code](/applications/advanced-concepts/locale.md).
In machine translation, they are used in building monolingual [training data](/customisation/training-data.md) from large collections of unidentified texts, such as webpages.
They are also used to automatically identify the source language in many machine translation systems.

## Challenges

If a particular locale is not supported in the language identification tool, it may be misclassified as another, similar locale.
For example, if a language identification tool does not support Serbian with the Cyrillic script, it may be misclassified as Macedonian.
Similarly, if a language identification tool does not support Hinglish, it may be misclassified as English.

## to include

- Why not use HTML language codes? They're unreliable
- Common approaches? are machine learning models that use character ngrams, word list matching, basic script tests, etc
