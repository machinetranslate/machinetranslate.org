---
grand_parent: Resources
parent: Concepts
title: Attention
description: A mechanism for improving the encoder-decoder model performance in machine translation
---

In an encoder-decoder architecture, the encoder takes the input sequence and creates a fixed-length context [vector](/concepts/vector.md), also called a **thought vector**.
The context vector represents the summary of the entire input sequence.
The decoder then uses this vector to generate the output.
One limitation of this design is that the system cannot retain information from longer input sequences.

The **attention** mechanism addresses this issue.
It weighs the importance of different parts of the input sequence and focuses on the relevant subsets instead of using the entire input equally.

## Process

- Scoring encoder hidden states depending on the relevant input word for each decoding step
- Producing a fixed-size context vector based on the weighted sum of all encoder hidden states
- Feeding the context vector into the decoder at each time step

## Approaches

 - Global attention
 - Local or window-based attention

While global attention considers all hidden states to generate the context vector, local attention takes only a subset.
