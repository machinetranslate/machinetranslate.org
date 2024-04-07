---
nav_order: 3
has_children: no
title: Calls for papers
description: Calls for papers for machine translation events and publications
seo:
    type: ItemList
    name: Calls for papers for machine translation events and publications
---

{% assign current_date = "now" | date: "%Y-%m-%d" %}
{% assign all_events = site.data.events | concat: site.data.wmt_events | where_exp: "event", "event.calls_for_papers_deadline" | concat: site.data.calls_for_papers %}
{% assign sorted_events = all_events | sort: "calls_for_papers_deadline" | reverse %}


### Calls for papers

| Deadline | Publication |
| --- | --- | --- |
{%- for event in sorted_events -%}{% if current_date  < event.calls_for_papers_deadline %}
| **{{ event.calls_for_papers_deadline | date: "%d %B %Y" }}** | **[{{ event.name }}]({% if event.id -%}/{{ event.id }}{% else -%}{{ event.url }}{% endif -%})** | {% else %}
| {{ event.calls_for_papers_deadline | date: "%d %B %Y" }} | [{{ event.name }}]({% if event.id %}/{{ event.id }}{% else %}{{ event.url }}{% endif -%}) | {% endif %}{% endfor %}