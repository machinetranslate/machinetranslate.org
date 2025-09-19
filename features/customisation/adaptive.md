---
grand_parent: Features
parent: Customisation
community_search_term: adaptive
title: Adaptive machine translation
description: Machine translation with online learning
featured: true
---

An **adaptive machine translation** system learns from human feedback and adapts its output on the fly.
Adaptive machine translation is applicable to [post-editing](/post-editing) workflows.

In adaptive machine translation, the system is customised while the human post-editor fixes the machine translation output, instead of after batch retraining.

Adaptive machine translation is an example of online machine learning and human-in-the-loop (HITL).

### API support

Adaptive machine translation first became practical with the rise of [neural machine translation](/neural-machine-translation).

[ModernMT](/modernmt) launched its adaptive feature in 2014.
[Lilt](/lilt) launched its adaptive machine translation feature in 2017.
[Amazon Translate](/amazon) launched Active Custom Translation in 2020.
[SYSTRAN](/systran) launched Neural Fuzzy Adaptation in 2021.
[Language Weaver](/language-weaver) launched its adaptive feature in 2022.

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

### Quality estimation

<ul>
  {% assign adaptive_qe_apis = site.data.quality_estimation | where: "adaptive", true %}
  {% for qe in adaptive_qe_apis %}
    <li>
      <a href="/quality-estimation/{{ qe.id }}">
          {{ qe.name }}
      </a>
    </li>
  {% endfor %}
</ul>

### Workflow

1. The system generates a machine translated output.
2. The output is fixed or approved.
3. The system learns from the correction.
4. The system reduces the chance of repeating the error.

Adaptive machine translation reduces the time a human takes to edit a machine translation suggestion.
