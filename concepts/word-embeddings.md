---
grand_parent: Resources
parent: Concepts
title: Word embeddings
description:
---

**Word-embeddings** are a way to represent language words as [vectors](vector.md) of real numbers.

## One-hot encoding

One-hot encoding is one simple method of representing every word from a vocabulary.
The goal is to convert the [vocabulary](vocabulary.md) into a format that can be used as input for machine learning models, which typically require numerical data.

One-hot encoding is a unique style of encoding information.
In one-hot encodings, only one position in the vector equals `1`, and the rest of the positions are `0`.


Example: `bird = 00010`

The length of a one-hot encoding vector is equal to the vocabulary size.

### Example

|    |    |    |    |    |    |
| -- | -- | -- | -- | -- | -- |
| `dog` | `0` | `1` | `0` | `0` | `0` |
| `bird` | `0` | `0` | `1` | `0` | `0` |
| `fish` | `0` | `0` | `0` | `1` | `0` |
| `deer` | `0` | `0` | `0` | `0` | `1` |
| `crocodile` | `0` | `0` | `0` | `0` | `0` |

The sample vectors contain 5 dimensions.
This size implies that the vocabulary contains 5 words.

### Challenges

- Large vocabularies need longer one-hot encoding vectors.
- One-hot encoding vectors consist of mostly 0.
As a result, operations with one-hot encoded vectors are very inefficient.
- One-hot encoding vectors do not represent text meaning or similarity.

### Embedding matrices

The goal of word embeddings is to capture meaning and context.
Further word information can be represented in a multi-dimensional vector.
As a result, word embedding lengths are shorter than one-hot encodings.

### Example

|    | pets | mammals | horns |
| -- | -- | -- | -- |
| `dog` | `1` | `1` | `0` |
| `bird` | `1` | `0` | `0` |
| `fish` | `1` | `0` | `0` |
| `deer` | `0` | `1` | `1` |
| `crocodile` | `0` | `0` | `0` |

The sample vectors contain 3 digits.
Similar concepts will have similar vectors.

In [neural machine translation](/approaches/neural-machine-translation.md), embedding matrices are usually learned during training.
