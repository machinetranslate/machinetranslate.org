---
nav_order: 2
parent: Contributing
title: Coming soon
community_search_exclude: true
description: Articles that are coming soon to Machine Translate
---

These articles are on the [roadmap](/roadmap.md) and are coming soon!

<ol>
{% for page in site.pages %}
  {% if page.layout == 'coming_soon' %}  
    <li>
      <h3>
        <a href="{{ page.url }}">{{ page.title }}</a>
      </h3>
    </li>
  {% endif %}
{% endfor %}
</ol>
