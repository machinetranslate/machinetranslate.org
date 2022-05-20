---
nav_order: 50
has_children: true
title: Languages
description: Machine translation language support
---

<ul>
{% for language in site.data.languages %}
{% assign language = language[1] %}
  <li>
    <a href="/{{ language.name | slugify }}">
      {{ language.name }}
    </a>
  </li>
{% endfor %}
</ul>
