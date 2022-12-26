---
grand_parent: Building and research
parent: Customisation
title: Tokenisation
description: Splitting a string into a sequence of tokens
---

Tokenisation is the process of splitting a string into a sequence of substrings called tokens.
A token is typically an atomic unit of meaning such as a word or punctuation character.

Example:
- input: `"Yes, but why?"`
- output: `["Yes", ",", "but", "why", "?"]`

Tokenization has a large effect on the vocabulary size of the machine translation system.
For example, if punctuation is not split off from words the vocabulary size will be much larger.
If the vocabulary size is larger, much more data is necessary to learn a machine translation model that will generalize.

## Challenges
The most basic tokenisation algorithm is splitting the string on whitespace.
Splitting on spaces is a reasonable baseline for many languages but will lead to an overly large vocabulary in other languages.
Two types of challenging languages are non-space-segmented languages and agglutinative languages.

Non-space-segmented languages include Chinese, Japanese, Korean, and Thai.
Tokenization is typically addressed by use of more advanced algorithms in these languages, often called word segmentation algorithms.

Agglutinative languages include Finnish and Hungarian.
Machine translation in these languages typically splits tokens into smaller units of meaning using algorithms such as [byte-pair encoding](/approaches/byte-pair-encoding.md).
