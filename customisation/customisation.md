---
nav_order: 1
parent: Features
has_children: true
title: Customisation
description: Customisation of machine translation
seo:
  name: Customisation of machine translation
---

{% assign customisable_apis = site.data.apis | where: "customisation_languages", true | where: "glossary", true | concat: site.data.apis | where: "formality", true | concat: site.data.apis | where: "adaptive", true | concat: site.data.apis | where: "fine-tuning", true %}

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

---

### See also

- [Features of machine translation APIs](/features/features.md)
