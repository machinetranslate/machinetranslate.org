---
nav_exclude: true
title: Machine Translate
description: Open resources and community for machine translation
permalink: /
seo:
  type: Organization
---

# Machine Translate

**Machine Translate** is building **open resources and community for machine translation**.

The content covers everything about machine translation, from products to research, and from history to news.

> #### Featured events
> - [Bay Area machine translation meetup](/bay-area-meetup-2) - 21 October, online
> - [WMT22](/wmt22) - December, Abu Dhabi
>
> #### Featured articles
> - [Adaptive machine translation](/customisation/adaptive.md)
> - [Quality estimation](/quality/quality-estimation.md)
> - [Companies](/industry/companies.md)


## Community

Read news, ask and answer questions and share your work!

<center>
  <button id="airtable-button">
     Join the community
  </button>
</center>
<script src="https://static.airtable.com/js/embed/embed_snippet_v1.js"></script><iframe id="airtable-iframe" class="airtable-embed airtable-dynamic-height" src="https://airtable.com/embed/shrJnYBtqU69rhDFw?backgroundColor=blue" frameborder="0" onmousewheel="" width="100%" height="986" style="background: transparent; border: 1px solid #ccc; display: none; margin-top: 20px;"></iframe>
<script>
    airtable_iframe = document.getElementById("airtable-iframe");
    airtable_button = document.getElementById("airtable-button");
    airtable_button.addEventListener("click", function() {
        if (airtable_iframe.style.display === "block") {
            airtable_iframe.style.display = "none";
        } else {
            airtable_iframe.height = "986";
            airtable_iframe.style.display = "block";
        }
    })
</script>


## Updates

Hear about news and events by following Machine Translate!

<center>
  <div class="social-links">
    {% include twitter.html %}
    {% include linkedin.html %}
    {% include facebook.html %}
  </div>
</center>

## Contributing

Machine Translate is open-source.
You can create or edit the content.

{% include contributions.html %}

<div style="display: flex; justify-content: center; gap: 20%;">
  <div>
    <center>
      👩🏻‍💻
      <h1>{{ site.github.contributors | size }}</h1>
      contributors
    </center>
  </div>
  <div>
    <center>
      ✏️
      <h1>{{ all_contributions }}</h1>
      contributions
    </center>
  </div>
</div>

[**Learn more about contributing →**](/contributing/contributing.md)

Watch and star the content source repository, browse and subscribe to issues and more!

<center>
  <div class="social-links">
    {% include github.html %}
  </div>
</center>



## About Machine Translate

Machine Translate is on a mission to make machine translation more accessible to more people.

Our mission is supported by people like you.

[**Learn more about the foundation →**](/about.md)
