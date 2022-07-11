---
grant_parent: Approaches
parent: Neural machine translation
title: Byte-pair encoding
description: A data compression algorithm for tokenisation for machine translation
---

**Byte-pair encoding** (BPE) is a data compression algorithm.
In byte-pair encoding, a byte that does not exist in the data replaces the most common consecutive pair of bytes.
Byte-pair encoding was first introduced in the article titled “_A new Algorithm for Data Compression_” by Philip Gage in the February 1994 edition of C Users Journal.

## Algorithm

1. Initialise the vocabulary with the frequency of word occurences in the corpus.
2. Represent each word in the corpus as a concatenation.
Use the special token `</w>` to identify the word end.
3. Split each word into characters and count the character occurence.
4. Look for the most frequent pairing, merge them and perform the same iteration again.
5. Repeat step 4 until all the iterations are performed or the token limit size is reached.

### Example

String: `aaabdaaabac`

1. The most frequent byte pair is `aa`. It is replaced `Z`. The string is now `ZabdZabac`.
2. The new most frequent byte pair is `ab`. It is replaced by `Y`. The string is now `ZYdZYac`.
3. `ZY` is encoded as `X` applying recursive byte-pair encoding. The string is now `XdXac`.
4. `XdXac` cannot be compressed further.

To decompress the data, the string characters are replaced in reverse order.


## Subword tokenisation

The use of byte-pair encoding ensures that the most common words in the vocabulary are presented as single tokens, whereas the rarest words are broken down into subword tokens.
Byte-pair encoding works well for both character-level and word-level representations, and it can manage large corpora.
Byte-pair encoding follows a greedy approach where it goes through every possible option at each iteration.

Implementation of byte-pair encoding is slightly modified to fit for subword tokenisation.
In subword tokenisation, frequently occurring subwords are merged instead of replaced by another byte.

### Example

Unigram: `praise`

1. The unigram is split up into more frequent subwords.
2. The unigram is represented as `['__sow', 'pr', 'ai', 'se', 'd', '__eow']`.
The `'__sow'` and `'__eow'` markers indicate the start and the end of the tokens.
