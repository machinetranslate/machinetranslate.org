---
grand_parent: Approaches
parent: Neural machine translation
title: Byte-pair encoding
description: A data compression algorithm for tokenisation for machine translation
---

**Byte-pair encoding** (BPE) is a data compression algorithm where the most common consecutive pair of bytes is replaced by a byte that is not seen in the data.
Byte-pair encoding was first introduced in the article titled "_A new Algorithm for Data Compression_" by Philip Gage in the February 1994 edition of C Users Journal.

Below are the steps that shows how the algorithm works:

1. Initialise the vocabulary with the frequency of occurence of words in the corpus.
2. Represent each word in the corpus as a concatenation with special token `</w>`.
3. Split each word into character and count their occurence.
4. Look for the most frequent pairing, merge them and perform the same iteration again.
5. Repeat 4 until all the iterations are performed or the token limit size is reached.

## Examples

String: `aaabdaaabac`

1. The most frequent byte pair is `aa`, which can be replaced by `Z`. The new string is now `ZabdZabac`.
2. The new most frequent byte pair is `ab` so we replace it by `Y` such that, we now have `ZYdZYac`. 
3. Applying recursive byte pair encoding to encode `ZY` as `X`, we now have `XdXac`. 
4. `XdXac` cannot be compressed further and to decompress the data, replacement in reverse order is performed. 

### Subword tokenisation

The use of byte-pair encoding in natural language processing (NLP) ensures that the most common words in the vocabulary are presented as single token whereas the rarest words are broken down into subword tokens.
Byte-pair encoding works well for both character-level and word-level representations and it can manage large corpora.
Byte-pair encoding follows greedy approach to find the best possible solution where it goes through every possible option to merge at each iteration by looking at its frequency.

Implementation of byte-pair encoding is slightly modified to fit for subword tokenisation.
In subword tokenisation, frequently occurring subwords are merged instead of replaced by another byte.

## Examples

Unigram: `praise` 

1. The unigram is split up into more frequent subwords. 
2. The unigram is represented as `['__sow', 'pr', 'ai', 'se', 'd', '__eow']`, where `'__sow'` and `'__eow'` are the markers for start and end of the tokens.
