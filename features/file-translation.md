---
nav_order: 3
parent: Features
title: File translation
description: Machine translation API support for translating entire files
---

**File translation** is the translation of entire files, including layout and formatting.

A growing number of machine translation APIs support translating various file types directly.

## File Types

File translation can involve various file types:

- Text
- Markdown
- HTML
- XML
- JSON
- Microsoft Office
- Image

The translation process can be manual, involving the writing of specific translation programs for each file pair, or automated using generalised translation algorithms and machine learning techniques.

{% assign apis = site.data.apis | where_exp: 'api', 'api.file_translation == true' %}

### API Support
<details>
<summary>{{apis.size}} machine translation APIs support file translation.</summary>

{% capture api_content %}
{% for api in apis %}
- [{{ api.name }}](/{{ api.id }})
{% endfor %}
{% endcapture %}

{{ api_content | markdownify }}

</details>
