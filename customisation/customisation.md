---
nav_order: 13
has_children: true
title: Customisation
description: Machine translation customisation
---

{% assign customisable_apis = site.data.apis | where: "customisation_languages", true | where: "glossary", true | concat: site.data.apis | where: "formality", true | concat: site.data.apis | where: "adaptive", true %}

{{ customisable_apis | size }} APIs support customisation.

<ul>
  {% for api in customisable_apis %}
    <li>
    <a href="/{{ api.id }}">
        {{ api.name }}
    </a>
    </li>
  {% endfor %}
</ul>
