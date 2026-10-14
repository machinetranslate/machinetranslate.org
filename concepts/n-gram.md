---
parent: Concepts
title: N-gram
community_search_term: "N-grams"
description: A short sequence of word types
render_latex: true
---

An **n-gram** is a short sequence of word types.
`n` is the number of words in the sequence, for example, a 2-gram has two word types.
N-grams have many applications in machine translation:

- [language models](/language-model), such as an [n-gram maximum likelihood estimate](/language-model#n-gram-maximum-likelihood-estimate)
- translation models for [statistical machine translation](/statistical-machine-translation)
- evaluation [metrics](/metrics), such as [BLEU](/bleu)
- [language identification](/language-identification)

| Number of words | Common name | Sequence notation | N-gram language model notation |
| ----------- | ----------- | ----------- | ----------- |
| 1 | Unigram | $$(w)$$ | $$P(w)$$ |
| 2 | Bigram | $$(w_1, w_2)$$ | $$P(w \vert w_{-1})$$ |
| 3 | Trigram | $$(w_1, w_2, w_3)$$ | $$P(w \vert w_{-1}, w_{-2})$$ |

## Example

[String](/string) in English: `"The car has two doors."`

[Tokens](/tokenisation): `"The", "car", "has", "two", "doors", "."`

Unigrams: `"The", "car", "has", "two", "doors", "."`

Bigrams: `("The", "car"), ("car", "has"), ("has", "two"), ("two", "doors"), ("doors", ".")`
