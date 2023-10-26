---
grand_parent: Building and research
parent: Approaches
nav_order: 100
title: Rule-based machine translation
description: Rule-based approaches to machine translation
---

**Rule-based machine translation** or **rules-based machine translation** (**RBMT**) is a machine translation approach based on hardcoded linguistic rules.

### Requirements

- Monolingual and bilingual dictionaries to map input words to output words
- Rules that represent the input language structure
- Rules that represent the output language structure

Rules describe the grammatical structure of the input and output languages and use a dictionary to translate the terms.

### Process

- A parser analyses the grammatical input structure.
- The parser creates an intermediate representation of the message.
This representation can have different levels of abstraction.
- The parser transfers that representation into the output language structure.

### Strategies

Direct approach - The source language input is translated word by word in the target language.

Transfer approach - The source language and the target language messages are transferred into intermediate representations.
The difference with interlingual MT is that the
transfer approach depends on the language pair involved.

Interlingual approach - The source language input is transformed into a semantic representation of the text, an interlingua.
The interlingua is the basis for generating the target text.

### Challenges

Rule-based machine translation is challenging because it demands time and effort.

Rule-based systems are not scalable because rules must be manually written.
Improvements require more rules and more human involvement.
