---
grand_parent: Resources
parent: Concepts
title: N-gram
description: A short sequence of word types
---

An **n-gram** is a short sequence of word types.
`n` is the number of words in the sequence, for example, a 2-gram has two word types.
N-grams have many applications in machine translation:

- [language models](/concepts/language-model), such as an [n-gram maximum likelihood estimate](/concepts/language-model#n-gram-maximum-likelihood-estimate)
- translation models for [statistical machine translation](/approaches/statistical-machine-translation.md)
- evaluation [metrics](/quality/metrics/metrics.md), such as [BLEU](/quality/metrics/bleu.md)
- language identification

<!-- Note: "https://render.githubusercontent.com/render/math?math=..." wasn't working on all equations so we switched to "https://latex.codecogs.com/svg.image?..." but it requires escaping to survive the Markdown table processor -->

| Number of words | Common name | Sequence notation | N-gram language model notation |
| ----------- | ----------- | ----------- | ----------- | 
| 1 | Unigram | <img src="https://latex.codecogs.com/svg.image?%28w%29" /> | <img src="https://latex.codecogs.com/svg.image?P%28w%29" /> |
| 2 | Bigram | <img src="https://latex.codecogs.com/svg.image?%28w_1%2C%20w_2%29" /> | <img src="https://latex.codecogs.com/svg.image?P%28w%20%5Cvert%20w_%7B-1%7D%29" /> |
| 3 | Trigram | <img src="https://latex.codecogs.com/svg.image?%28w_1%2C%20w_2%2C%20w_3%29" /> | <img src="https://latex.codecogs.com/svg.image?P%28w%20%5Cvert%20w_%7B-1%7D%2C%20w_%7B-2%7D%29" /> |

## Example

[String](/concepts/string.md) in English: `"The car has two doors."`

[Tokens](/customisation/tokenisation): `"The", "car", "has", "two", "doors", "."`

Unigrams: `"The", "car", "has", "two", "doors", "."`

Bigrams: `("The", "car"), ("car", "has"), ("has", "two"), ("two", "doors"), ("doors", ".")`

