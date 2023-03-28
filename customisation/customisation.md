---
nav_order: 60
has_children: true
title: Customisation
description: Machine translation customisation
---

{% assign customizable_apis = site.data.apis | where: "customization_languages" | where "glossary" | concat: site.data.apis | where "formality" | concat: site.data.apis | where "adaptive" %}

{{ customizable_apis | size }} APIs support customization.

<ul>
  {% for api in customizable_apis %}
    <li>
    <a href="/{{ api.id }}">
        {{ api.name }}
    </a>
    </li>
  {% endfor %}
</ul>
