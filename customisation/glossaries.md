---
grand_parent: Building and research
parent: Customisation
layout: coming_soon
title: Glossaries
description: Terminology lists for training and customising machine translation
---
#Glossaries

Glossaries are lists of terms in one language aligned to their translation in one or more languages. They can be added to machine translation systems.
Adding a glossary to a commercial machine translation provider can increase the terminology accuracy of the output.

## Application

Glossaries are leveraged at translation time, and no training is required.
When a glossary term is matched in the source sentence, its translation is enforced in the output.

The insertion of a glossary term in the output happens regardless of the context.
The terms included in the glossary should therefore be unambiguous and context-independent, as in the following examples:
- Respiratory syndrome
- Balance sheet
- Paraffin

Ambiguous terms can have a negative impact on the output:
- Spread
- Cookies
- Surface treatment

##Term matching and insertion

Several machine translation providers offer the possibility to enhance their output using a glossary.
The way in which the glossary is leveraged may differ in terms of source term matching and target term insertion.

In some cases the source term is matched in the source text only if it occurs with the same morphology and ortography as in the glossary.
Some providers match the source term regardless of the morphology and ortography of its occurrence in the source sentence.

The target term can be inserted either with the same form as in the glossary, or by adapting the term to the rest of the sentence and viceversa, for example ensuring a correct agreement between the subject and the verb.

## Glossary term forms

If the source and target terms are used with the same form as in the glossary, the latter should cover the following forms, depending on the language:
- Morphology
  - Singular and plural forms
  - Masculine and feminine forms
  - Verb inflections
- Ortography
  - Casing (uppercased, lowercased, capitalised, not capitalised)

If the term is matched regardless of its form and is inflected so that it agrees with the rest of the items in the target sentence, it is possible to include in the glossary only the dictionary form of each term.
