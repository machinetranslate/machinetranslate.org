---
nav_order: 2
has_children: false
title: Events
description: List of machine translation events
featured: true
seo:
    type: ItemList
    name: List of machine translation events
---

{% assign amta_events = site.data.events | where_exp: "event", "event.name contains 'AMTA'" | sort: 'name' | reverse  %}
{% assign eamt_events = site.data.events | where_exp: "event", "event.name contains 'EAMT'" | sort: 'name' | reverse  %}
{% assign mt_summit_events = site.data.events | where_exp: "event", "event.name contains 'MT Summit'" | sort: 'name' | reverse  %}

{% if amta_events.size > 0 %}
### AMTA
<details>
<summary>Events</summary>

{% capture amta_content %}
{% for event in amta_events %}
{% if event.id %}
- [{{ event.name }}](/{{ event.id }}) <br>
{% else %}
- **{{ event.name }}**
{%- endif -%}{% endfor %}
{% endcapture %}

{{ amta_content | markdownify }}

</details>
{% endif %}


{% if eamt_events.size > 0 %}
### EAMT
<details>
  <summary>Events</summary>

{% capture eamt_content %}
{% for event in eamt_events %}
{% if event.id %}
- [{{ event.name }}](/{{ event.id }}) <br>
{% else %}
- **{{ event.name }}**{%- endif -%}{% endfor %}
{% endcapture %}

{{ eamt_content | markdownify }}

</details>
{% endif %}

{% if mt_summit_events.size > 0 %}
### MT Summit
<details>
  <summary>Events</summary>

{% capture mtsummit_content %}
{% for event in mt_summit_events %}
{% if event.id %}
- [{{ event.name }}](/{{ event.id }}) <br>
{% else %}
- **{{ event.name }}**
{%- endif -%}{% endfor %}
{% endcapture %}

{{ mtsummit_content | markdownify }}

</details>
{% endif %}

{% assign all_events = site.data.events | concat: site.data.wmt_events %}
{% assign events_by_year = all_events | sort: "start_date" | reverse | group_by_exp: "event", "event.start_date | date: '%Y'" %}
{% assign current_date = site.time | date: "%Y-%m-%d" %}

{% for year in events_by_year %}
## {{ year.name }} events

{% assign sorted_events = year.items | sort: "start_date" | reverse %} 
| Date | Event | Location |
| --- | --- | --- |
{% for event in sorted_events %}
  {%- capture startDay -%}{{- event.start_date | date: "%d" -}}{%- endcapture -%}
  {%- capture endDayMonth %}{{- event.end_date | date: "%d %B" -}}{% endcapture -%}{%- if event.end_date -%}{%- if event.start_date != event.end_date -%}
  {%- capture date_range -%}{{ startDay }} - {{ endDayMonth }}{%- endcapture -%}{%- else -%}
  {%- capture date_range -%}{{ event.start_date | date: "%d %B" }}{%- endcapture -%}{%- endif -%}{%- else -%}
  {%- capture date_range -%}{{ event.start_date | date: "%d %B" }}{%- endcapture -%}{%- endif -%}
| {{ date_range }} | {% if event.id %}{% if event.start_date > current_date %}**[{{ event.name }}](/{{ event.id }})**{% else %}[{{ event.name }}](/{{ event.id }}){% endif %}{% else %}{% if event.start_date > current_date %}**{{ event.name }}**{% else %}{{ event.name }}{% endif %}{% endif %} | {% if event.location.online %}Online{% else %}{{ event.location.location }}{% endif %} | 
{% endfor %}{% endfor %}

## 2005 events

| Date | Event | Location |
| ---- | ---- | ---- |
| 29 - 30 June | **WPT05** | Ann Arbor, Michigan |
| 30 - 31 May | EAMT 2005 | Budapest, Hungary |

## 2004 events

| Date | Event | Location |
| ---- | ---- | ---- |
| 28 September – 2 October | AMTA 2004 - “Machine translation: from real users to research” | Washington, District of Columbia |
| 26 - 27 April | EAMT 2004 | Valletta, Malta |

## 2003 events

| Date | Event | Location |
| ---- | ---- | ---- |
| 15 - 17 May | EAMT 2003 | Dublin, Ireland |

## 2002 events

| Date | Event | Location |
| ---- | ---- | ---- |
| 14 - 15 November | EAMT 2002 | Manchester, England |
| 8 - 12 October | AMTA 2002 - “Machine translation: from research to real users” | Tiburon, California |

## 2001 events

| Date | Event | Location |
| ---- | ---- | ---- |
| 18 - 23 September | MT Summit 2001 | Galicia, Spain |

## 2000 events

| Date | Event | Location |
| ---- | ---- | ---- |
| 10 - 14 October | AMTA 2000 - “Envisioning machine translation in the information future” | Cuernavaca, Mexico |
| 11 - 12 May | EAMT 2000 | Ljubljana, Slovenia |

## 1999 events

| Date | Event | Location |
| ---- | ---- | ---- |
| 22 - 23 April | EAMT 1999 | Prague, Czech Republic |

## 1998 events

| Date | Event | Location |
| ---- | ---- | ---- |
| 28 - 31 October | AMTA 1998 - “Machine translation and the information soup” | Langhorne, Pennsylvania |
| 2 - 3 April | EAMT 1998 | Geneva, Switzerland |

## 1997 events

| Date | Event | Location |
| ---- | ---- | ---- |
| 21 - 22 May | EAMT 1997 | Copenhagen, Denmark |

## 1996 events

| Date | Event | Location |
| ---- | ---- | ---- |
| 2 - 5 October | AMTA 1996 - “Expanding MT horizons” | Montreal, Quebec |
| 29 - 30 August | EAMT 1996 | Vienna, Austria |

## 1995 events

| Date | Event | Location |
| ---- | ---- | ---- |
| 10 - 13 July | MT Summit 1995 | Luxembourg, Luxembourg |

## 1994 events

| Date | Event | Location |
| ---- | ---- | ---- |
| 5 - 8 October | AMTA 1994 - “Technology partnerships for crossing the language barrier” | Columbia, Maryland |
| 14 - 16 September | EAMT 1994 | Hildesheim, Germany |

## 1993 events

| Date | Event | Location |
| ---- | ---- | ---- |
| 26 - 28 April | EAMT 1993 | Heidelberg, Germany |

## 1989 events

| Date | Event | Location |
| ---- | ---- | ---- |
| 16 - 18 August | MT Summit 1989 | Munich, Germany |

## Frauds

### ICMTCS

The International Conference on Machine Translation and Cognitive Science is a fraudulent event created by [WASET](https://en.wikipedia.org/wiki/World_Academy_of_Science,_Engineering_and_Technology).

> The publisher has been listed as a "potential, possible, or probable" predatory publisher by Jeffrey Beall and is listed as such by the Max Planck Society and Stop Predatory Journals.

WASET was registered in Azerbaijan by a family of scammers operating out of Turkey.
