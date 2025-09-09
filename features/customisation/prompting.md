---
grand_parent: Features
parent: Customisation
layout: coming_soon
title: Prompting
description:
---

## API support
{% assign prompt_apis = site.data.apis | where: "prompt_required", true %}
<ul>
  {% for api in prompt_apis %}
    <li>
    <a href="/{{ api.id }}">
        {{ api.name }}
    </a>
    </li>
  {% endfor %}
</ul>