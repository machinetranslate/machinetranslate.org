---
nav_order: 4
has_children: true
parent: Application areas
title: Translation and localisation
description: Machine translation for translation and localisation
---

Machine translation is a key technology in professional **translation and localisation** workflows.

### Integrations

Translation software, like [translation management systems](/integrations) (TMS) and computer-aided translation tools (CAT), integrate [machine translation APIs](/apis), directly or via plugins.

### Workflow

The translation software fills in the machine translation for the human translator to [post-edit](/workflows/post-editing.md).
The machine translation can be inserted in whole files at once or one [segment](../concepts/segment.md) at a time.
Some systems that translate segment-by-segment can learn from post-edits and adapt the machine translation output accordingly.

### Productivity
<!-- Not always true!!! Link to the chapter on post-editing productivity when it's ready -->
Post-editors can work three to four times faster than traditional translators.

### Definitions

#### Translation

**Translation** is the transformation of a text in its original language into the same text in the target language.

#### Localisation

**Localisation** is the transformation of an object from one cultural environment to another.
An object is a document, a software, a film, a book, and so on.

In localisation, the object retains its most salient features, and the cultural-unfit features are replaced, as far as possible, by their adequate counterparts.

A software localisation process consists of the following steps:

1. Identifying if the software is useful in the target culture.
2. Identifying the features that need to be replaced or adapted.
3. Translating user interface and user assistance content.
4. Replacing or adapting the features that can’t be used in the target culture.
5. Creating versions of the software in the target [locale](/advanced-concepts/locale.md) that are target culture specific.
6. Testing the localised versions:
   - Verifying the validity of the translation in the context of the software.
   - Checking if the new versions work well for the target audience in each language:
     - Special characters used in the user interface, instructions, and input fields
     - Number, time, and date formats. Currency and units of measurements that are specific to the target culture
     - List and glossary order that is specific to the target culture
     - Text that is written from right to left, if applicable

## See also

- [Connecting machine translation APIs to translation software ](../resources/integration/cat-tools.md)
