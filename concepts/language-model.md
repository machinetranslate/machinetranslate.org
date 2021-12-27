---
description: Language model
---

# Language model

A language model tries to predict the next word given the already produced history.
For example, given the text span `the man with` a language model's output could be `a: 0.4, the: 0.3, my: 0.1, his: 0.05, ...`.
This would mean that the article `a` has a 40% probability of being the continuation and is the most likely.

It is possible to do *decoding*, which means repeatedly taking e.g. the most probable output, adding it to the text and so on.
This way a language model can generate new text.

# Models

There are many different ways in which language models are created.

## N-gram Maximum Likelihood Estimate

The easiest one is to count a number of occurrences of the pair $(w_1, w_2)$ and divide that by the number of occurrences of just $w_1$.
The result is the probability that with the history (now truncated to just $w_1$) the next word is $w_2$.
Considering only the most recent history is called the Markov assumption.

This model is quite limited because it can't reasonably consider any even mid-term sentence dependencies. 
We may extend this to consider longer histories, e.g. 3-grams but there are numerous issues that arise there.
One solution to those is language model smoothing.

## Neural Language Model

A neural language model is a neural network that computes the next word probability.
RNN-based approaches worked by considering the whole sentence history compressed into a single vector.
They perform badly on long-term dependency phenomena.
This was vastly improved with the advent of attention.
State of the art neural language models are based on the Transformer architecture, either the encoder (e.g. BERT) or the decoder (e.g. GPT).

# Language Models in Machine Translation

## [Phrase-Based Machine Translation](../general/statistical.md)

Phrase-based machine translation relies on a decoding algorithm that tries to cover the original sentence with phrases.
That can be done trivially by using single-word phrases.
The key missing ingredient is the cohesion between phrases, called fluency.
Therefore, in the decoding phase of phrase-based machine translation, the score of a state is determined partly by the language model probability.
Higher probabilities are prefered because they correspond to more natural-sounding sentences.

In phrase-based machine translation it is fairly easy to manipulate the weights of adequacy vs. fluency by changing the corresponding coefficients in the scoring function.

## [Neural Machine Translation](../general/neural.md)

The usage of language models in neural machine translation is more subtle.
The decoder can be viewed as a language model because the output is a probability across the target vocabulary and it has computational access to the history: $p(t_i|s_{1\ldots |s|}, t_{1\ldots (i-1)})$.