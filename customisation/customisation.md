---
nav_order: 60
has_children: true
title: Customisation
description: Machine translation customisation
---

{% assign customizable_apis = site.data.apis | where: "customization_languages", true | where: "glossary", true | concat: site.data.apis | where: "formality", true | concat: site.data.apis | where: "adaptive", true %}

{{ customizable_apis | size }} APIs support customisation.

<ul>
  {% for api in customizable_apis %}
    <li>
    <a href="/{{ api.id }}">
        {{ api.name }}
    </a>
    </li>
  {% endfor %}
</ul>
