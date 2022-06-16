---
grand_parent: Building and research
parent: Customisation
layout: coming_soon
title: Glossaries
description: Terminology lists for training and customising machine translation
---
#Glossaries

Glossaries, i.e. lists of terms in one language aligned to their translation in one or more languages, can be added to machine translation systems.
When a glossary term is matched in the source sentence, its translation is enforced in the output.

## How glossaries are leveraged by MT systems
Glossaries are leveraged at translation time, and no training is required.
Adding a glossary to a commercial MT provider can increase the terminology accuracy of the output.
However, the insertion of a term in the output happens regardless of the context.
The terms included in the glossary should therefore be unambiguous, meaning that their translation should not be heavily dependent on the context.
For example, "respiratory syndrome" is a good candidate to appear in a glossary, whereas the translation of the word "spread" may differ when it is used as a verb or a noun, or when the term occurs in the medical or in the financial domain.


Several MT providers offer the possibility to enhance their output using a glossary.
The way in which the glossary is leveraged may differ in terms of source term matching and target term insertion.
In some cases the source term is matched in the source text only if it occurs with the same morphology and ortography as in the glossary.
Some providers match the source term regardless of the morphology and ortography of its occurrence in the source sentence.


The target term can be inserted either with the same form as in the glossary, or by adapting the term to the rest of the sentence and viceversa, for example ensuring a correct agreement between the subject and the verb.

## Term forms to be included in a glossary for MT
If the source and target terms are used with the same form as in the glossary, the latter should cover all possible morphological and ortographical forms of each term.
If the term is matched regardless of its form and is inflected, if needed, so that it agrees with the rest of the items in the sentence, it is possible to include in the glossary only the dictionary form of each term.