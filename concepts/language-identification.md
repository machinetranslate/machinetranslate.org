---
parent: Customisation
title: Language identification
description: Identifying the language of a text
---

**Language identification** tools identify the [language](/locale) of an unknown text.
In machine translation, language identification tools are used in building monolingual [training data](/training-data) from large collections of unidentified texts such as webpages.
Language identification tools are also used to automatically identify the source language in many machine translation systems when the source language is unspecified.

As of 2023, language identification is typically implemented as a text classifier over character [n-grams](/n-gram).
Alternative approaches include dictionary lookup, word n-grams, statistical models, and rule-based identification.

## Challenges

- Similar languages may be mistaken for one another, for example [Dutch](/dutch) and [Afrikaans](/afrikaans).
- Language identification is harder on shorter texts because there may not be enough language-specific information.
Longer texts have more chances of having language-specific characters and words, making it easier to identify.
- If a particular [locale](/locale) is not supported in the language identification tool, it may be misclassified as another, similar locale.
For example, if a language identification tool does not support [Serbian](/serbian) with the Cyrillic script, it may be misclassified as [Macedonian](/macedonian).
