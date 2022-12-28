---
grand_parent: Resources
parent: Concepts
title: N-gram
description: A short sequence of word types
---

An **n-gram** is a short sequence of word types.
`n` is the number of words in the sequence, for example, a 2-gram has two word types.
N-grams are commonly used in [language models](/concepts/language-model), for example in an [n-gram maximum likelihood estimate](/concepts/language-model#n-gram-maximum-likelihood-estimate).
N-grams are also used in language identification and translation models for [statistical machine translation](/approaches/statistical-machine-translation.md).

The table below has common names and notation:

| Number of words | Common name | Sequence notation | N-gram language model notation |
| ----------- | ----------- | ----------- | ----------- | 
| 1 | Unigram | <img src="https://render.githubusercontent.com/render/math?math=(w)"> | <img src="https://render.githubusercontent.com/render/math?math=P(w)"> |
| 2 | Bigram | <img src="https://render.githubusercontent.com/render/math?math=(w_1, w_2)"> | <img src="https://render.githubusercontent.com/render/math?math=P(w \vert w_-1)"> |
| 3 | Trigram | <img src="https://render.githubusercontent.com/render/math?math=(w_1, w_2, w_3)"> | <img src="https://render.githubusercontent.com/render/math?math={P(w \vert w_-1, w_-2)}"> |
