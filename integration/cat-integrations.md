# __How to connect MTs to CAT tools__  


> ___&ldquo;The biggest challenge is to combine technology and the human side without losing the latter&rdquo;___ — Gordana Antonijević  





# Introduction  
Machine Translation (MT) technology allows you to automatically translate your text from one language to another. Both Trados Studio 2021™ and memoQ translator pro 9.8™ use plugins to connect to machine translation engine vendors. This manual provides information as to how to obtain API keys from MT vendors and enter them into the plugins. 

## MT vendors described  
This manual shows how to obtain APIs to the following MTs:

| API | Language pairs | Customization | Setup | Cost | Privacy |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| Google Cloud Translation Basic (Google Translate API v2)  | 100+  | Translation memory and glossary  | Difficult | $20 per 1M characters | No-trace, ISO 27001 and GDPR-compliant |
| DeepL  |  26 | Glossary  | Easy | EUR 8.99 per user/5 files a month EUR 29.99 per user/20 files EUR 59.99 per user/100 files | No-trace, ISO 27001 and GDPR-compliant |
| Amazon Translate (AWS)   |  75 | Glossaries, Adaptive customization, to and from English only  | Difficult | $15 per 1 M characters, $60 for adaptive customization per 1 M characters | Amazon shared responsibility model, ISO 27001-compliant |
| Modern MT   |  40+ | Glossaries, Adaptive customization for all pairs  | Easy | $25 per month for professionals/unlimited no. of characters, $50 for real-time adaptive | No-trace, ISO 27001 and GDPR-compliant |

# Privacy
More information on how the MT vendors listed in [MT vendors described](#mt-vendors-described) process your data is available from:

 - for DeepL:
 [https://www.deepl.com/pro-data-security/](https://www.deepl.com/pro-data-security/)
 - for Google Cloud Translation Basic (or Google Translate API v2):
 [https://cloud.google.com/translate/data-usage](https://cloud.google.com/translate/data-usage)
 - Amazon Translate (AWS):
 [https://docs.aws.amazon.com/translate/latest/dg/data-protection.html](https://docs.aws.amazon.com/translate/latest/dg/data-protection.html)
 - Modern MT:
 [https://www.modernmt.com/privacy/](https://www.modernmt.com/privacy/)


# [How to set up Trados Studio 2021™ plugins](trados.md)  


# [How to set up memoQ Translator Pro 9.8™ plugins](memoq.md)  


# [How to obtain API keys for MT plugins](api-keys.md)  


# References  


- [https://docs.memoQ.com/current/en/Places/modernmt-settings.html](https://docs.memoQ.com/current/en/Places/modernmt-settings.html), accessed on 29/09/2021
- [https://helpcenter.memoQ.com/hc/en-us/articles/360019498179-How-to-set-up-the-DeepL-MT-plugin](https://helpcenter.memoQ.com/hc/en-us/articles/360019498179-How-to-set-up-the-DeepL-MT-plugin), accessed on 27/09/2021
- [https://blog.api.rakuten.net/api-tutorial-google-translate-api/](https://blog.api.rakuten.net/api-tutorial-google-translate-api/), accessed on 28/09/2021
- [https://community.sdl.com/product-groups/translationproductivity/f/openexchange_applications/27164/deepl-plugin-not-working](https://community.sdl.com/product-groups/translationproductivity/f/openexchange_applications/27164/deepl-plugin-not-working), accessed on 25/09/2021
- [https://helpcenter.memoQ.com/hc/en-us/articles/360010267380-Installing-Google-Translate-API-plugin-in-memoQ](https://helpcenter.memoQ.com/hc/en-us/articles/360010267380-Installing-Google-Translate-API-plugin-in-memoQ), accessed on 29/09/2021
- [https://community.sdl.com/product-groups/translationproductivity/f/trados-live/30935/google-translate-api---how-to-activate-in-sdl-trados-live](https://community.sdl.com/product-groups/translationproductivity/f/trados-live/30935/google-translate-api---how-to-activate-in-sdl-trados-live), accessed on 29/09/2021
- [https://docs.aws.amazon.com/translate/latest/dg/API_Reference.html](https://docs.aws.amazon.com/translate/latest/dg/API_Reference.html), accessed on 28/09/2021
- [https://docs.aws.amazon.com/translate/latest/dg/translate-dg.pdf](https://docs.aws.amazon.com/translate/latest/dg/translate-dg.pdf), accessed on 27/09/2021
- [https://docs.weblate.org/en/latest/admin/machine.html#aws](https://docs.weblate.org/en/latest/admin/machine.html#aws), accessed on 30/09/2021
- [https://community.sdl.com/product-groups/translationproductivity/w/customer-experience/3315/amazon-translate-mt-provider](https://community.sdl.com/product-groups/translationproductivity/w/customer-experience/3315/amazon-translate-mt-provider), accessed on 28/09/2021
- [https://docs.aws.amazon.com/general/latest/gr/rande.html](https://docs.aws.amazon.com/general/latest/gr/rande.html), accessed on 30/09/2021
- [https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html), accessed on 30/09/2021
- [https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html), accessed on 29/09/2021
- [https://www.deepl.com/pl/pro/change-plan#team](https://www.deepl.com/pl/pro/change-plan#team), accessed on 30/09/2021
- [https://translatepress.com/docs/automatic-translation/generate-google-api-key/](https://translatepress.com/docs/automatic-translation/generate-google-api-key/), accessed on 28/09/2021
- [https://community.sdl.com/product-groups/translationproductivity/f/openexchange_applications/30609/google-translate-api-not-available-in-sdl-trados-2021?ReplySortBy=CreatedDate&ReplySortOrder=Ascending](https://community.sdl.com/product-groups/translationproductivity/f/openexchange_applications/30609/google-translate-api-not-available-in-sdl-trados-2021?ReplySortBy=CreatedDate&ReplySortOrder=Ascending), accessed on 26/09/2021
- [https://gateway.sdl.com/apex/communityknowledge?articleName=000005906](https://gateway.sdl.com/apex/communityknowledge?articleName=000005906), accessed on 25/09/2021
- [https://cloud.google.com/docs/authentication/api-keys#creating_an_api_key](https://cloud.google.com/docs/authentication/api-keys#creating_an_api_key), accessed on 29/09/2021
- [https://www.modernmt.com/api/#introduction](https://www.modernmt.com/api/#introduction), accessed on 27/09/2021
- [https://www.youtube.com/watch?v=-KHq094SeWU](https://www.youtube.com/watch?v=-KHq094SeWU), accessed on 26/09/2021
- [https://www.deepl.com/pl/pro-tool_integration.html](https://www.deepl.com/pl/pro-tool_integration.html), accessed on 27/09/2021
- [https://developers.google.com/tech-writing/one/short-sentences](https://developers.google.com/tech-writing/one/short-sentences), accessed on 26/09/2021
- [https://modernmt-website.s3.amazonaws.com/downloads/ModernMT+Plugin+Guide+for+SDL+Trados+Studio.pdf](https://modernmt-website.s3.amazonaws.com/downloads/ModernMT+Plugin+Guide+for+SDL+Trados+Studio.pdf), accessed on 28/09/2021
- [https://docs.memoQ.com/ggl-tst/Places/mt-settings.html](https://docs.memoQ.com/ggl-tst/Places/mt-settings.html), accessed on 29/09/2021 


