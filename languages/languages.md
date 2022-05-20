---
nav_order: 50
has_children: true
title: Languages
description: Machine translation language support
---

<ul>
{% for language in site.data.languages %}
  <li>
    <a href="/{{ language.name | slugify }}">
      {{ language.code }} {{ language.name }}
    </a>
  </li>
{% endfor %}
</ul>
