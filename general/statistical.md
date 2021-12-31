---
title: Statistical machine translation
description: Statistical approaches to machine translation
---

**Statistical machine translation** is a machine translation approach that uses large volumes of bilingual data to find the most probable translation for a given input. Statistical machine translation systems learn to translate by analyzing the statistical relationships between original texts and their existing human translations.

The most important components in statistical machine translation are the translation model and the language model.

### Language model

The language model is built from the output language monolingual data. The language model finds the best choice from the candidate translations based on the translation language. The language model can be associated with fluency in the translation because it gives the translated text its natural language flow.

### Translation model

The statistical machine translation engine is trained with [parallel data](/customization/parallel-data.md) to create a translation model. A translation model is a table of aligned phrases and their translation. These phrases are called [n-grams](concepts/n-gram.md). The purpose of the translation model is to predict candidate translations for specific input texts. The translation model can be associated with adequacy because it preserves the meaning of the source.


### Process

- The input text is divided into phrases.
- The phrases are matched with their parallel equivalents from the translation model.
- The language model validates that the translation is probable in the output language.


### Approaches

- Word-based translation: The model generates the translation word-by-word.
- Phrase-based translation: The model translates sequences of words.
- Syntax-based translation: The model translates syntactic units.
- Hierarchical phrase-based translation: The model combines phrase-based methods with syntax-based methods.

### Challenges

- Parallel data creation and training is costly and time-consuming.
- Statistical machine translation requires large parallel data of at least 2 million words.
- Specific errors in the translation are hard to predict and fix.
- Statistical machine translation is less suitable for language pairs with differences in word order, for instance, English to Chinese translations.
