---
parent: Input modes
layout: coming_soon
nav_order: 1
has_toc: false
title: Text
description: Text-to-text machine translation, text-to-speech machine translation, text-to-image machine translation
---

{% assign apis = site.data.apis | where_exp: 'api', 'api.inputs contains "text"' %}

### API support
<details>
<summary>{{apis.size}} machine translation APIs support file translation.</summary>

{% capture api_content %}
{% for api in apis %}
- [{{ api.name }}](/{{ api.id }})
{% endfor %}
{% endcapture %}

{{ api_content | markdownify }}

</details>