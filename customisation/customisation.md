---
nav_order: 1
parent: Features
has_children: true
title: Customisation
description: Customisation of machine translation
seo:
  name: Customisation of machine translation
---

**Customisation** of machine translation is used to accurately translate for the domain and reflect a specific terminology and style.

The most common type of customisation is [fine-tuning](fine-tuning.md) on [parallel data](parallel-data.md).

{% assign customisable_apis_size = site.data.apis | where: "customisation_languages", true | concat: site.data.apis | where: "glossary", true | concat: site.data.apis | where: "formality", true | concat: site.data.apis | where: "adaptive", true | concat: site.data.apis | where: "fine-tuning", true %}

{{ customisable_apis | size }} machine translation APIs support customisation.
