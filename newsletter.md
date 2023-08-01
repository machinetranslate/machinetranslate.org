---
nav_order: 100
has_children: false
nav_exclude: true
title: Newsletter
description: Machine Translate newsletter
---

Sign up to our monthly machine translation newsletter.

You will get a list of upcoming events, due calls for papers, job opportunities, the most interesting community posts, and more!

<center>
  <button id="airtable-button">
     Get the newsletter
  </button>
</center>
<script src="https://static.airtable.com/js/embed/embed_snippet_v1.js"></script><iframe id="airtable-iframe" class="airtable-embed airtable-dynamic-height" src="https://airtable.com/embed/shry2NkGYBfnhPina?backgroundColor=blue" frameborder="0" onmousewheel="" width="100%" height="533" style="background: transparent; border: 1px solid #ccc; display: none; margin-top: 20px;"></iframe>
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

Also join our [community](community.md)!