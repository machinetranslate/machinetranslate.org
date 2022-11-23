---
grand_parent: Resources
parent: Concepts
layout: coming_soon
title: Word embeddings
description:
---

# Word Embeddings

Artificial Neural Networks (ANNs) are designed to learn from numerical data. There is, therefore, a need to represent words in a special input representation which is suitable for the ANNs to be consumed. For this purpose, word embeddings are learned. In essence, they are models that are created to map a set of words or phrases in a vocabulary to vectors of numerical values. The input unit to a neural network in the area of NMT are words or sub-words. Words are discrete tokens, which can be portrayed by their index in the respective source or target vocabulary. In order for neural networks to differentiate between different words, these vectors must be unambiguous and mathematically truly independent in terms of vector distances. One-hot encoding is used to achieved this.

# One-hot encoding

The aim of One-hot encoding is to represent each word from a vocabulary 𝑊 by a |𝑊|-dimensional vector 𝑣 with almost all entries set to zero. There are
separate vocabularies used for the source and target language, e.g. `𝑊_𝑠𝑜𝑢𝑟𝑐𝑒` or `𝑊_𝑡𝑎𝑟𝑔𝑒𝑡`. Only a single position 𝑘 in the vector 𝑣 is set to one. It identifies the 𝑘_𝑡ℎ word 𝑤_𝑘 ∈ 𝑊 from the vocabulary. The length of the vector 𝑣 corresponds with the vocabulary size |𝑊|. The ordering of words in the vocabulary must be defined once and remain unchanged during training and inference but is otherwise arbitrary. One-hot encoded vectors are usually
the word input for the neuronal networks in NMT. 

# Embedding matrices 

Numerical operations with such one-hot encoded vectors for these words would be very inefficient because most values in the one-hot vector are equal 0. As
a result, the matrix calculation occurring between the one-hot vector and the first hidden layer will result in an output having mostly 0 values. Therefore, an embedding layer is introduced to greatly improve the efficiency of the network. Embeddings are just like a fully-connected layer with small differences. In detail, its activation functions are linear and a bias vector is usually not used. The dimension of the embedding layer is usually
configured to be significantly smaller than the size of the respective input word vocabulary.

In NMT, embedding matrices are usually trained jointly with the rest of the network using backpropagation and stochastic gradient descent. In other areas of NLP, pre-trained word embeddings, such as e.g. word2vec, trained on unlabelled text have become popular.
