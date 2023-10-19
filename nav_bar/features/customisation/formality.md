---
grand_parent: Features
parent: Customisation
title: Formality
description:
---

Machine translation APIs that offer the **formality** feature allow customising the machine translation output level of formality.

Some APIs offer three options:

- Formal
- Informal
- Default

The formality feature is not usually available in all languages supported by a machine translation API.

## API support

<ul>
  {% assign formality_apis = site.data.apis | where: "formality", true %}
  {% for api in formality_apis %}
    <li>
    <a href="/{{ api.id }}">
        {{ api.name }}
    </a>
    </li>
  {% endfor %}
</ul>