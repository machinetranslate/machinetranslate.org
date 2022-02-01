---
grand_parent: Approaches
parent: Neural machine translation
layout: coming_soon
title: Byte-pair encoding
description: A data compression algorithm for machine translation
---

Byte-pair encoding (BPE) is a data compression algorithm where the most common consecutive pair of bytes is replaced by a byte that is not seen in the data.
It was first introduced in the article titled "A new Algorithm for Data Compression" by Philip Gage in the February 1994 edition of C Users Journal.

A very well-known example of BPE data compression is, suppose we have a string "aaabdaaabac" which is compressed such that, the most frequent byte pair "aa" is replaced by Z. We now have "ZabdZabac". 
The new most frequent byte pair is "ab" so we replace it by Y such that, we now have "ZYdZYac". 
Applying recursive byte pair encoding to encode ZY as X, we now have "XdXac". It cannot be compressed further and to decompress the data, replacement in reverse order is performed. 

The use of BPE in NLP ensures that the most common words in the vocabulary are presented as single token whereas the rarest words are broken down into subword tokens instead of introducing it as "<UNK>" tokens.
BPE works well for both character-level and word-level representations and it can manage large corpora.
It follows greedy approach to find the best possible solution where it goes through every possible option to merge at each iteration by looking at its frequency.

Here are the steps that demonstrates how the algorithm works:

1. Initialise the vocabulary with the frequency of occurence of words in the corpus.
2. Represent each word in the corpus as a concatenation with special token "</w>".
3. Split each word into character and count their occurence.
4. Look for the most frequent pairing, merge them and perform the same iteration again.
5. Repeat 4 until all the iterations are performed or the token limit size is reached.

BPE is a widely used subword-tokenization algorithms.
This algorithm ensures that every word (rare or frequent) are not forgotten!
