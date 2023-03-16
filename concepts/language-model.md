---
parent: Concepts
title: Language model
description: Probability of a word in a sequence
---

# Language model

A language model takes text input and outputs the next word or character.
The input is often called a “context” or “history”, because it represents what has been written so far.

Example:
- input: `the man is riding a ___`
- output: `bike` 40%, `car`: 30%, `scooter`: 10%, `blue`: 0.5%, ...

In this example, the word `bike` has a 40% probability of being the next word and is the most likely.

## Decoding

Decoding is used to convert an abstract representation into text.
It is done, for example, by repeatedly taking the most probable output, adding it to the text and so on.
This way a language model can generate new text as in the following example:

- Step 6
  - input: `<BOS> the man is riding a ___`
  - output: `bike`: 40%, `car`: 30%, ...
- Step 7
  - input: `<BOS> the man is riding a bike ___`
  - output: `to`: 20%, `on`: 10%, ...
- Step 8:
  - input: `<BOS> the man is riding a bike to ___`
  - output: `the`: 30%, `a`: 25%, ...
- ...
- Step 11:
  - input: `<BOS> the man is riding a bike to the store . ___`
  - output: `<EOS>`: 98%, ...

For the beginning the special [token](/customisation/tokenisation.md) `<BOS>` (beginning of sentence) is used.
When another special token `<EOS>` (end of sentence), the decoder stops.

This kind of decoding where only the most probable token is considered is called **greedy decoding** and it may not always lead to the most fluent output.
For this reason, the algorithm **beam search** is used that considers multiple most probable outputs at the same time.

# Models

There are many different ways in which language models are created.

## N-gram maximum likelihood estimate


The easiest one is to count a number of occurrences of a phrase, in this case a pair,
<img src="https://render.githubusercontent.com/render/math?math=(w_1, w_2)"> and divide that by the number of occurrences of just
<img src="https://render.githubusercontent.com/render/math?math=w_1">.
The result is the probability that with the history (now truncated to just <img src="https://render.githubusercontent.com/render/math?math=w_1">) the next word is <img src="https://render.githubusercontent.com/render/math?math=w_2">.

Under the **Markov assumption**, the input is limited to the last word only.
This model is quite restricted because it can’t model well any even mid-term sentence dependencies.
There are models that take longer input, e.g. [3-grams](n-gram.md), but they have create new issues, such as data sparsity.
One solution to those is **language model smoothing**.

## Neural language model

A neural language model is a neural network that computes the probability of the next word.
RNN-based approaches worked by considering the whole sentence history compressed into a single [vector](vector.md).
They perform badly on long-term dependency phenomena.
This was vastly improved with the advent of [attention](attention.md).
State-of-the-art neural language models are based on the [Transformer architecture](/approaches/transformers.md), either the encoder (e.g. BERT) or the decoder (e.g. GPT).

# Language models in machine translation

## Phrase-based machine translation

[Phrase-based machine translation](/approaches/statistical-machine-translation.md) relies on a decoding algorithm that tries to cover the original sentence with phrases.
That can be done trivially by using single-word phrases.
The key missing ingredient is the cohesion between phrases, called “fluency”.
Therefore, in the decoding phase of phrase-based machine translation, the score of a state is determined partly by the language model probability.
Higher probabilities are preferred because they correspond to more natural-sounding sentences.

In phrase-based machine translation, increasing the weight of the language model increases fluency but can decrease adequacy.

## Neural machine translation

The usage of language models in [neural machine translation](/approaches/neural-machine-translation.md) is more subtle.
The decoder can be viewed as a language model because the output is a probability across the target [vocabulary](vocabulary.md) and it has computational access to the history: <img src="https://render.githubusercontent.com/render/math?math=p(t_i|s_{1\ldots |s|}, t_{1\ldots (i-1)})">.
