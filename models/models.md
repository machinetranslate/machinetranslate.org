---
nav_order: 12
has_children: true
permalink: /:basename
title: Models
description: Large language models
---

Machine translation **models** are machine learning models for generating a translation.

[APIs](/apis) provide convenient access to underlying models. Models can also be trained and deployed directly.

## Evolution

With [statistical machine translation](/statistical-machine-translation), systems required multiple models:

- [Language model](/statistical-machine-translation#language-model)
- [Translation model](/statistical-machine-translation#translation-model)

With [neural machine translation](/neural-machine-translation), that was replaced by one end-to-end model. Increasingly, one model is used for many language pairs.

Unlike machine translation APIs or apps, raw machine translation models typically still do not handle basic requirements of a production system, like [language identification](/language-identification), [segmentation](/segment) or [bridging](/bridging).

Each model typically consists of multiple model versions, that vary by size or release date.

## More types

In addition to neural machine translation models, there are various types of models currently used by machine translation APIs and related APIs.

- Generic generative AI (chat) models, that require prompting to generate translations
- Translation-focused generative AI (chat) models
- [Quality evaluation](/quality-evaluation) models
- [Quality estimation](/quality-estimation) models
- [Automatic post-editing](/automatic-post-editing) models

