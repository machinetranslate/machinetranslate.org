---
parent: Customisation
title: Adaptive machine translation
description: Machine translation with online learning
featured: true
---

An **adaptive machine translation** system learns from human feedback and adapts its output on the fly.
Adaptive machine translation is applicable to [post-editing](../workflows/post-editing.md) workflows.

In adaptive machine translation, the system is customised while the human post-editor fixes the machine translation output, instead of after batch retraining.

Adaptive machine translation is an example of online machine learning and human-in-the-loop (HITL).
### API support

Adaptive machine translation first became practical with the rise of [neural machine translation](/approaches/neural-machine-translation.md).
[Lilt](/apis/lilt.md) launched the first adaptive feature in 2017.

[ModernMT](/apis/modernmt.md) launched its adaptive feature in 2019.
[Amazon Translate](/apis/amazon.md) launched Active Custom Translation in 2020.
[SYSTRAN](/apis/systran.md) launched Neural Fuzzy Adaptation in 2021.
[Language Weaver](/apis/language-weaver.md) launched its adaptive feature in 2022.

<ul>
  {% assign adaptive_apis = site.data.apis | where: "adaptive", true %}
  {% for api in adaptive_apis %}
    <li>
    <a href="/{{ api.id }}">
        {{ api.name }}
    </a>
    </li>
  {% endfor %}
</ul>

### Workflow

1. The engine generates a machine translated output.
2. The output is fixed or approved.
3. The engine learns from the correction.
4. The system reduces the chance of repeating the error.

Adaptive machine translation reduces the time a human takes to edit a machine translation suggestion.
