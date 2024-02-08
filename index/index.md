---
nav_exclude: true
community_search_exclude: true
title: Machine Translate
description: Open information and community for machine translation
permalink: /
seo:
  type: Organization
---

# Machine Translate

The **Machine Translate Foundation** is building **open information** and **community** for machine translation.

{% assign integration_count = 0 %}
{% for tms in site.data.integrations %}
  {% assign s = tms.api_integrations | size %}
  {% assign integration_count = integration_count | plus: s %}
{% endfor %}

<style>
  .big {
    font-size: 2em;
    background: -webkit-linear-gradient(45deg, #DA291C, #ed7f78, #DA291C, #71150f);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
</style>

<div style="display: flex; justify-content: center; gap: 20%; padding: 1em;">
  <div>
    <center>
      <a href="/apis">
        <span class="big">{{ site.data.apis | size }}</span><br/>
        APIs
      </a>
    </center>
  </div>
  <div>
    <center>
      <a href="/integrations">
        <span class="big">{{ integration_count }}</span><br/>
        integrations
      </a>
    </center>
  </div>
  <div>
    <center>
      <a href="/languages">
        <span class="big">{{ site.data.languages | size }}</span><br/>
        languages
      </a>
    </center>
  </div>
</div>

The content covers everything about machine translation, from products to research, and from history to news.

> #### Featured events
> - [AMTA 2024](/amta-2024) - 30 September-02 October, Chicago 🇺🇸
> - [EAMT 2024](/eamt-2024) - 24-27 June, Sheffield 🇬🇧
> - [Adaptive machine translation panel](/meetup) - 8 February, online 🌎

> #### Featured articles
> - [Integrations](/integrations)
> - [Features](/features)
> - [Adaptive machine translation](/adaptive)
> - [Quality estimation](/quality-estimation)


## Stay connected

Join the community to ask and answer questions, and share your work.

[**Join the community →**](/community)

<div style="display: flex; justify-content: center; gap: 20%;">
  <div>
    <center>
      <a href="/community">
        👥<br/>
        <span class="big">Community</span>
      </a>
      <br/>
      <span class="hint">700+ members</span>
    </center>
  </div>
</div>

Sign up to the newsletter to catch key news of the month.

[**Get the newsletter →**](/newsletter)

<div>
  <div>
    <center>
      <a href="/newsletter">
        📧<br/>
        <span class="big">Newsletter</span>
      </a>
      <br/>
      <span class="hint">1000+ readers</span>
    </center>
  </div>
</div>

Follow the Machine Translate Foundation on other platforms.

<center>
  <div class="social-links">
    {% include twitter.html %}
    {% include linkedin.html %}
    {% include facebook.html %}
  </div>
</center>


---


## About the Machine Translate Foundation

The Machine Translate Foundation is on a mission to make machine translation more accessible to more people.

Our mission is supported by people like you.

[**About the foundation →**](/about)

Machine Translate is open-source.
You can create or edit the content.

{% include contributions.html %}

<div style="display: flex; justify-content: center; gap: 20%;">
  <div>
    <center>
      👩🏻‍💻<br/>
      <span class="big">{{ site.github.contributors | size }}</span><br/>
      contributors
    </center>
  </div>
  <div>
    <center>
      ✏️<br/>
      <span class="big">{{ all_contributions }}</span><br/>
      contributions
    </center>
  </div>
</div>

Watch and star the content source repository, browse and subscribe to issues and more!

[**Contributing →**](/contributing)

<center>
  <div class="social-links">
    {% include github.html %}
  </div>
</center>
