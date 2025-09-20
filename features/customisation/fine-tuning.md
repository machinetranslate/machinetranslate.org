---
grand_parent: Features
parent: Customisation
layout: coming_soon
title: Fine-tuning
description:
---

## Machine translation
{% assign fine_tuning_apis = site.data.apis | where: "fine-tuning", true %}
<summary>
  <strong>{{ fine_tuning_apis | size }}</strong> machine translation APIs support fine-tuning.
</summary>
<ul>
  {% for api in fine_tuning_apis %}
    <li>
    <a href="/{{ api.id }}">
        {{ api.name }}
    </a>
    </li>
  {% endfor %}
</ul>

## Quality estimation
{% assign fine_tuning_qe_apis = site.data.quality_estimation | where: "fine-tuning", true %}
<summary>
  <strong>{{ fine_tuning_qe_apis | size }}</strong> quality estimation APIs support fine-tuning.
</summary>
<ul>
  {% for qe in fine_tuning_qe_apis %}
    <li>
      <a href="/quality-estimation/{{ qe.id }}">
          {{ qe.name }}
      </a>
    </li>
  {% endfor %}
</ul>