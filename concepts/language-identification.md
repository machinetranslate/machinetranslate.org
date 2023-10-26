---
parent: Customisation
title: Language identification
description: Identifying the language of a text
---

**Language identification** tools identify the [language](/applications/advanced-concepts/locale.md) of an unknown text.
In machine translation, language identification tools are used in building monolingual [training data](../features/customisation/training-data.md) from large collections of unidentified texts such as webpages.
Language identification tools are also used to automatically identify the source language in many machine translation systems when the source language is unspecified.

As of 2023, language identification is typically implemented as a text classifier over character [n-grams](/concepts/n-gram.md).
Alternative approaches include dictionary lookup, word n-grams, statistical models, and rule-based identification.

## Challenges

- Similar languages may be mistaken for one another, for example [Dutch](/languages/dutch.md) and [Afrikaans](/languages/afrikaans.md).
- Language identification is harder on shorter texts because there may not be enough language-specific information.
Longer texts have more chances of having language-specific characters and words, making it easier to identify.
- If a particular [locale](/applications/advanced-concepts/locale.md) is not supported in the language identification tool, it may be misclassified as another, similar locale.
For example, if a language identification tool does not support [Serbian](/languages/serbian.md) with the Cyrillic script, it may be misclassified as [Macedonian](/languages/macedonian.md).
