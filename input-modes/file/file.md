---
parent: Input modes
nav_order: 3
has_toc: false
title: File
description: Machine translation API support for translating entire files
---

**File translation** is the translation of entire files, including layout and formatting.

A growing number of machine translation APIs support translating various file types directly.

## File types

There is support for plain text files as well as the most common document formats.
- Text and Markdown files
- HTML and XML files
- JSON and YAML files
- Microsoft Word and PowerPoint files
- PDF files

Image files and audio files are typically not supported.

{% assign apis = site.data.apis | where_exp: 'api', 'api.inputs contains "file"' %}

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
