---
nav_order: 1
parent: Tutorials
has_children: true
title: Connecting engines to translation software
description: How to connect machine translation engines to computer-aided translation tools
---


> ___&ldquo;The biggest challenge is to combine technology and the human side without losing the latter&rdquo;___ — Gordana Antonijević  



Machine Translation technology allows users to automatically translate text from one language to another.
Both Trados and memoQ use plugins to connect to machine translation engine vendors.
This tutorial provides information as to how to obtain application programming interfaces (API) keys from machine translation vendors and enter them into the plugins.


#### [How to set up Trados plugins](/trados-tutorial)  

#### [How to set up memoQ plugins](/memoq-tutorial)  

#### [How to obtain API keys for MT plugins](/api-keys)  


### MT vendors described

| API | Language pairs | Customization | Setup | Cost | Privacy |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| Google Cloud Translation Basic (Google Translate API v2)  | 100+  | Translation memory and glossary  | Difficult | $20 per 1M characters | No-trace, ISO 27001 and GDPR-compliant |
| DeepL  |  26 | Glossary  | Easy | EUR 8.99 per user/5 files a month EUR 29.99 per user/20 files EUR 59.99 per user/100 files | No-trace, ISO 27001 and GDPR-compliant |
| Amazon Translate (AWS)   |  75 | Glossaries, Adaptive customisation, to and from English only  | Difficult | $15 per 1 M characters, $60 for adaptive customisation per 1 M characters | Amazon shared responsibility model, ISO 27001-compliant |
| Modern MT   |  40+ | Glossaries, Adaptive customisation for all pairs  | Easy | $25 per month for professionals/unlimited no. of characters, $50 for real-time adaptive | No-trace, ISO 27001 and GDPR-compliant |

#### Privacy

More information on how the machine translation vendors process your data is available in their websites:

 - for DeepL:
 [https://www.deepl.com/pro-data-security/](https://www.deepl.com/pro-data-security/)
 - for Google Cloud Translation Basic (or Google Translate API v2):
 [https://cloud.google.com/translate/data-usage](https://cloud.google.com/translate/data-usage)
 - Amazon Translate (AWS):
 [https://docs.aws.amazon.com/translate/latest/dg/data-protection.html](https://docs.aws.amazon.com/translate/latest/dg/data-protection.html)
 - Modern MT:
 [https://www.modernmt.com/privacy/](https://www.modernmt.com/privacy/)


### References  


- [docs.memoQ.com/current/en/Places/modernmt-settings.html](https://docs.memoQ.com/current/en/Places/modernmt-settings.html), accessed on 8 February, 2023
- [helpcenter.memoQ.com/hc/en-us/articles/360019498179-How-to-set-up-the-DeepL-MT-plugin](https://helpcenter.memoQ.com/hc/en-us/articles/360019498179-How-to-set-up-the-DeepL-MT-plugin), accessed on 8 February, 2023
- [blog.api.rakuten.net/api-tutorial-google-translate-api/](https://blog.api.rakuten.net/api-tutorial-google-translate-api/), no longer accessible
- [community.sdl.com/product-groups/translationproductivity/f/openexchange_applications/27164/deepl-plugin-not-working](https://community.sdl.com/product-groups/translationproductivity/f/openexchange_applications/27164/deepl-plugin-not-working), no longer accessible
- [helpcenter.memoQ.com/hc/en-us/articles/360010267380-Installing-Google-Translate-API-plugin-in-memoQ](https://helpcenter.memoQ.com/hc/en-us/articles/360010267380-Installing-Google-Translate-API-plugin-in-memoQ), accessed on 8 February, 2023
- [community.sdl.com/product-groups/translationproductivity/f/trados-live/30935/google-translate-api---how-to-activate-in-sdl-trados-live](https://community.sdl.com/product-groups/translationproductivity/f/trados-live/30935/google-translate-api---how-to-activate-in-sdl-trados-live), no longer accessible
- [docs.aws.amazon.com/translate/latest/dg/API_Reference.html](https://docs.aws.amazon.com/translate/latest/dg/API_Reference.html), accessed on 8 February, 2023
- [docs.aws.amazon.com/translate/latest/dg/translate-dg.pdf](https://docs.aws.amazon.com/translate/latest/dg/translate-dg.pdf), accessed on 8 February, 2023
- [docs.weblate.org/en/latest/admin/machine.html#aws](https://docs.weblate.org/en/latest/admin/machine.html#aws), accessed on 8 February, 2023
- [community.sdl.com/product-groups/translationproductivity/w/customer-experience/3315/amazon-translate-mt-provider](https://community.sdl.com/product-groups/translationproductivity/w/customer-experience/3315/amazon-translate-mt-provider), no longer accessible
- [docs.aws.amazon.com/general/latest/gr/rande.html](https://docs.aws.amazon.com/general/latest/gr/rande.html), accessed on 8 February, 2023
- [docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html), accessed on 8 February, 2023
- [docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html), accessed on 8 February, 2023
- [deepl.com/en/pro/change-plan#team](https://www.deepl.com/en/pro/change-plan#team), accessed on 8 February, 2023
- [translatepress.com/docs/automatic-translation/generate-google-api-key/](https://translatepress.com/docs/automatic-translation/generate-google-api-key/), accessed on 8 February, 2023
- [community.sdl.com/product-groups/translationproductivity/f/openexchange_applications/30609/google-translate-api-not-available-in-sdl-trados-2021?ReplySortBy=CreatedDate&ReplySortOrder=Ascending](https://community.sdl.com/product-groups/translationproductivity/f/openexchange_applications/30609/google-translate-api-not-available-in-sdl-trados-2021?ReplySortBy=CreatedDate&ReplySortOrder=Ascending), no longer accessible
- [gateway.sdl.com/apex/communityknowledge?articleName=000005906](https://gateway.sdl.com/apex/communityknowledge?articleName=000005906), accessed on 8 February, 2023
- [cloud.google.com/docs/authentication/api-keys#creating_an_api_key](https://cloud.google.com/docs/authentication/api-keys#creating_an_api_key), accessed on 8 February, 2023
- [modernmt.com/api/#introduction](https://www.modernmt.com/api/#introduction), accessed on 8 February, 2023
- [youtube.com/watch?v=-KHq094SeWU](https://www.youtube.com/watch?v=-KHq094SeWU), accessed on 8 February, 2023
- [deepl.com/pl/pro-tool_integration.html](https://support.deepl.com/hc/en-us/sections/360005269360-CAT-tools), accessed on 8 February, 2023
- [developers.google.com/tech-writing/one/short-sentences](https://developers.google.com/tech-writing/one/short-sentences), accessed on 8 February, 2023
- [modernmt-website.s3.amazonaws.com/downloads/ModernMT+Plugin+Guide+for+SDL+Trados+Studio.pdf](https://s3.amazonaws.com/modernmt.prod.public.us-east-1/downloads/ModernMT+Plugin+Guide+for+RWS+Trados+Studio.pdf), accessed on 8 February, 2023
- [docs.memoQ.com/ggl-tst/Places/mt-settings.html](https://docs.memoQ.com/ggl-tst/Places/mt-settings.html), accessed on 8 February, 2023
