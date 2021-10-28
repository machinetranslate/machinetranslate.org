---
description: Cleaning training data
---

# Filtering

**Filtering** for machine translation is the process of cleaning relevant [parallel data](customization/parallel.data.md) for engine training.

Parallel data can be filtered manually or automatically.

### Tools

- Zipporah
- Bicleaner
- LASER

### Workflow

#### Pre-filtering

The pre-filter stage looks for obvious noise in parallel data:

- Too short or too long sentences.
- Sentences that have too few words
- Sentence pairs with mismatched lengths in terms of number of tokens
- Sentence pairs where names, numbers, dates, email addresses, URLs do not match between both sides
- Sentence pairs that are too similar, indicating copying instead of translating

Noisy sentence pairs can be fixed or dropped.

#### Scoring

Sentence pairs that pass the pre-filter stage are scored to automatically classify their quality.

#### Classification

High-quality sentence pairs are separated from low-quality sentence pairs.

#### Cleaning

Cleaning or fixing parallel data comprise the following techniques:

- Normalization
- [Tokenization](customization/tokenization.md)
- Removing duplicate segments
- Removing non-alphabetical symbols
- Removing irrelevant languages
- Spelling out or collapsing acronyms
- Replacing named entities with placeholders
- Matching the original and the translated sentences punctuation
- Fixing typos and spelling mistakes
