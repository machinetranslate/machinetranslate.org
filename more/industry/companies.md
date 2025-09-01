---
nav_order: 235
title: Companies
parent: More
description: List of machine translation companies
featured: true
search_exclude: true
seo:
  name: List of machine translation companies
---

**Machine translation companies** primarily provide machine translation or technology related to machine translation.

The history of machine translation companies begins in the defence and intelligence sector.

Other players, from technology giants like Meta to translation agencies to the European Union, increasingly build their own machine translation.

Since the advent of [statistical machine translation](/statistical-machine-translation) and [neural machine translation](/neural-machine-translation), there are growth companies backed by venture capital.

{% include collapsible_toc.html %}

{% for company in site.data.companies %}

{% assign offers = "" | split: "" %}
  {% if company.apis and company.apis.size > 0 %}
    {% assign c = company.apis.size %}
    {% if c == 1 %}
      {% assign phrase = c | append: " translation API" %}
    {% else %}
      {% assign phrase = c | append: " translation APIs" %}
    {% endif %}
    {% assign offers = offers | push: phrase %}
  {% endif %}
  {% if company.quality_estimation and company.quality_estimation.size > 0 %}
    {% assign c = company.quality_estimation.size %}
    {% if c == 1 %}
      {% assign phrase = c | append: " quality estimation API" %}
    {% else %}
      {% assign phrase = c | append: " quality estimation APIs" %}
    {% endif %}
    {% assign offers = offers | push: phrase %}
  {% endif %}
  {% if company.automatic_post_editing and company.automatic_post_editing.size > 0 %}
    {% assign c = company.automatic_post_editing.size %}
    {% if c == 1 %}
      {% assign phrase = c | append: " automatic post-editing API" %}
    {% else %}
      {% assign phrase = c | append: " automatic post-editing APIs" %}
    {% endif %}
    {% assign offers = offers | push: phrase %}
  {% endif %}
  {% if company.tms and company.tms.size > 0 %}
    {% assign c = company.tms.size %}
    {% if c == 1 %}
      {% assign phrase = c | append: " TMS/CAT" %}
    {% else %}
      {% assign phrase = c | append: " TMSes/CATs" %}
    {% endif %}
    {% assign offers = offers | push: phrase %}
  {% endif %}
  {% if company.routers and company.routers.size > 0 %}
    {% assign c = company.routers.size %}
    {% if c == 1 %}
      {% assign phrase = c | append: " Router" %}
    {% else %}
      {% assign phrase = c | append: " Routers" %}
    {% endif %}
    {% assign offers = offers | push: phrase %}
  {% endif %}
  {% if company.models and company.models.size > 0 %}
    {% assign c = company.models.size %}
    {% if c == 1 %}
      {% assign phrase = c | append: " Model" %}
    {% else %}
      {% assign phrase = c | append: " Models" %}
    {% endif %}
    {% assign offers = offers | push: phrase %}
  {% endif %}

## {{ company.name }}

- **Type:** {% if company.type and company.type.size > 0 -%}{% for t in company.type -%}{% assign cleaned = t | replace: "-", " " | downcase %}
    {% if forloop.first -%}
      {{ cleaned | capitalize }}{% else -%}{{ cleaned }}{% endif -%}{% unless forloop.last -%}, {% endunless %}{% endfor %}{% else %}N/A{% endif %}

- **Founded:** 
  {% if company.founded -%}
    {{ company.founded }}{% else %}N/A{% endif %}

- **Location:** 
  {% if company.location -%}
    {{ company.location }}{% else %}N/A{% endif %}

- **Offerings:**  {% if offers.size > 0 %} {{ offers | join: ", " }}{% else %} N/A{% endif %}

- **Links:** 
  {%- for url in company.urls %}{% assign domain = url | replace: "https://", "" | replace: "http://", "" | split: "/" | first | replace: "www.", "" %}
    [{{ domain }}]({{ url }}){% unless forloop.last %}, {% endunless %}{% endfor %}

{% endfor %}
