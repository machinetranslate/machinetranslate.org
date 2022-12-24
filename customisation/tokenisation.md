---
grand_parent: Building and research
parent: Customisation
title: Tokenisation
description: Splitting a string into a sequence of tokens
---

Tokenisation is the process of splitting a string into a sequence of tokens.
Tokens include words as well as punctuation characters.

Example:
- input: `"Yes, but why?"`
- output: `["Yes", ",", "but", "why", "?"]`

Machine translation algorithms learn the association between words in one language and words in another language.
Tokenisation is needed because machine translation cannot operate effectively on the space of all possible strings, but can operate effectively on the space of all possible tokens.

## Languages
The most basic tokenisation algorithm is splitting the string on whitespace.
Splitting on spaces is a reasonable baseline for many languages.
However, there are several languages that do not separate words with whitespace, such as Chinese, Japanese, Korean, and Thai.
Machine translation of non-space-segmented languages often relies on more complex word segmentation algorithms.

## See also

- [Byte-pair encoding](/approaches/byte-pair-encoding.md): Byte-pair encoding is related because it also splits strings into smaller units.
