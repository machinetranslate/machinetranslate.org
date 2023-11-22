---
nav_order: 3
parent: Contributing
title: Contributors
community_search_exclude: true
description: Contributors to the Machine Translate Foundation
---

{% include contributions.html %}

**{{ site.github.contributors | size }} contributors** have made **[{{ all_contributions }} contributions](https://github.com/machinetranslate/machinetranslate.org/graphs/contributors?type=a)** to the Machine Translate Foundation.

<div id='contributors'>
  {% for user in site.github.contributors %}
    <p>
      <a
          href='{{user.html_url}}'
          style='font-size: large; font-weight: bold;'
          name='{{user.login}}'>
        <image
          src='{{user.avatar_url}}'
          style='vertical-align: middle; width: 2em; max-width: 50%; margin-right: 0.5em; border-radius: 50%;'
        />
        {{user.login}}
      </a>
    </p>
  {% endfor %}
</div>

<!--- Random sort --->
<script>
  var div = document.getElementById('contributors');
  for (var i = div.children.length; i >= 0; i--) {
    div.appendChild(div.children[Math.random() * i | 0]);
  }
</script>
