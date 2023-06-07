---
nav_order: 100
has_children: false
nav_exclude: true
title: Community
description: Machine Translate community
---

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


Also sign up for your [newsletter](newsletter.md)!