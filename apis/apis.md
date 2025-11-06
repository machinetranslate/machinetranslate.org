---
nav_order: 11
has_children: true
title: Translation APIs
description: List of machine translation APIs
has_toc: false
seo:
    name: List of machine translation APIs
    type: ItemList
---

There is a growing set of machine translation APIs available and [integrated into translation management systems (TMS)](/integrations).

The most popular APIs are available as self-serve APIs and support more than 100 [languages](/languages) and more than 10000 language pairs.
By 2022, there was a self-serve API that supported more than 300 languages.

Besides language and [locale](/locale) support, the APIs also vary by [features](/features), like [customisation](/customisation), [privacy policies](/data-confidentiality) and whether or not they are self-service products.

Most of the underlying machine translation systems are now based on [neural machine translation](/neural-machine-translation).

---

Here the APIs are ordered by the number of languages and [locales](/locale) that each support.

{% assign api_pages = "" | split: "" %}

{% for page in site.pages %}
  {% if page.path contains 'apis/' %}
    {% unless page.path == 'apis/apis.md' %}
        {% assign api_pages = api_pages | push: page %}
    {% endunless %}
  {% endif %}
{% endfor %}

{% assign max_count = 0 %}
{% for page in api_pages %}
  {% assign lang_count = page.supported_languages | size | default: 0 %}
  {% if lang_count > max_count %}
    {% assign max_count = lang_count %}
  {% endif %}
{% endfor %}

{% for count in (0..max_count) reversed -%}
  {% for page in api_pages -%}
    {% assign lang_count = page.supported_languages | size | default: 0 -%}
    {% if lang_count == count %}
- [{{ page.title }}](/{{ page.id }}) {% if page.active == false %}`inactive`{% endif %}{% endif %}{% endfor %}{% endfor %}