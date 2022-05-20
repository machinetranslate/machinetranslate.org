---
nav_order: 50
has_children: true
title: Languages
description: Machine translation language support
---

<ul>
{% for language in site.data.languages %}
  <li>
    {{ language.code }}
    <a href="/{{ language.name | slugify }}">
      {{ language.name }}
    </a>
    {{ language }}
  </li>
{% endfor %}
</ul>
