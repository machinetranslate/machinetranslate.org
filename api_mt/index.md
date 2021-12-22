# __HOW TO CONNECT FOUR POPULAR MTs TO TRADOS STUDIO 2021™ AND MEMOQ TRANSLATOR PRO 9.8™__

> ___The biggest challenge is to combine technology and the human side without losing the latter___ — Gordana Antonijević, Head of Translation Unit, Veris



[1. INTRODUCTION](#1-introduction)

* [1.1 MT vendors described](#11-mt-vendors-described)

* [1.2 Privacy](#12-privacy)

[2. How to set up Trados Studio 2021™ plugins](#2-how-to-set-up-trados-studio-2021-plugins)  

* [2.1 Amazon Translate (AWS)](#21-amazon-translate-aws)

  -  [2.1.1 How to obtain an API key](#211-how-to-obtain-an-api-key)

   - [2.1.2 How to set up the Trados Studio 2021™ plugin for Amazon Translate (AWS)](#212-how-to-set-up-the-trados-studio-2021-plugin-for-amazon-translate-aws)
   
* [2.2 DeepL](#22-deepl)

  - [2.2.1 How to obtain an API key](#221-how-to-obtain-an-api-key)
  - [2.2.2 How to set up the Trados Studio 2021™ plugin for DeepL](#222-how-to-set-up-the-trados-studio-2021-plugin-for-deepl)

* [2.3 ModernMT](#23-modernmt)

  - [2.3.1 How to obtain an API key](#231-how-to-obtain-an-api-key)

  - [2.3.2 How to set up the Trados Studio 2021™ plugin for ModernMT](#232-how-to-set-up-the-trados-studio-2021-plugin-for-modernmt)

* [2.4 Google Cloud Translation Basic (or Google Translate API v2)](#24-google-cloud-translation-basic-or-google-translate-api-v2)

  - [2.4.1 How to obtain an API key](#241-how-to-obtain-an-api-key)

  - [2.4.2 How to set up the Trados Studio 2021™ plugin for Google Cloud Translation Basic (or Google Translate API v2)](#242-how-to-set-up-the-trados-studio-2021-plugin-for-google-cloud-translation-basic-or-google-translate-api-v2)

  - [2.4.3 How to set up the Google API Validator plugin for Trados Studio 2021™ (optional)](#243-how-to-set-up-the-google-api-validator-plugin-for-trados-studio-2021-optional)

[3. How to set up Memoq Translator Pro 9.8™ plugins](#3-how-to-set-up-memoq-translator-pro-98-plugins)  

* [3.1 Amazon Translate (AWS)](#31-amazon-translate-aws)

  -  [3.1.1 How to obtain an API key](#311-how-to-obtain-an-api-key)

  - [3.1.2 How to set up the Memoq Translator Pro 9.8™ plugin for Amazon Translate (AWS) (for a local profile)](#312-how-to-set-up-the-memoq-translator-pro-98-plugin-for-amazon-translate-aws-for-a-local-profile)

* [3.2 DeepL](#32-deepl)

   - [3.2.1 How to obtain an API key](#321-how-to-obtain-an-api-key)

  - [3.2.2 How to set up the Memoq Translator Pro 9.8™ plugin for DeepL](#322-how-to-set-up-the-memoq-translator-pro-98-plugin-for-deepl)

* [3.3 ModernMT](#33-modernmt)

  - [3.3.1 How to obtain an API key](#331-how-to-obtain-an-api-key)

  - [3.3.2 How to set up the Memoq Translator Pro 9.8™ plugin for ModernMT](#332-how-to-set-up-the-memoq-translator-pro-98-plugin-for-modernmt)

* [3.4 Google Cloud Translation Basic (or Google Translate API v2)](#34-google-cloud-translation-basic-or-google-translate-api-v2)

  - [3.4.1 How to obtain an API key](#341-how-to-obtain-an-api-key)

  - [3.4.2 How to set up the Memoq Translator Pro 9.8™ plugin for Google Cloud Translation Basic (or Google Translate API v2)](#342-how-to-set-up-the-memoq-translator-pro-98-plugin-for-google-cloud-translation-basic-or-google-translate-api-v2)

[4. How to obtain API keys for MT plugins](#4-how-to-obtain-api-keys-for-mt-plugins)  

* [4.1 Amazon Translate (AWS)](#41-amazon-translate-aws)

* [4.2 DeepL](#42-deepl)

* [4.3 ModernMT](#43-modernmt)

* [4.4 Google Cloud Translation Basic (or Google Translate API v2)](#44-google-cloud-translation-basic-or-google-translate-api-v2)

[5. References](#5-references)
## 1. INTRODUCTION
Machine Translation (MT) technology allows you to automatically translate your text from one language to another. Both Trados Studio 2021™ and memoQ translator pro 9.8™ use plugins to connect to machine translation engine vendors. This manual provides information as to how to obtain API keys from MT vendors and enter them into the plugins. 

*Disclaimer*  

Information contained herein is valid as of October 1st, 2021. Due to frequent changes in user interfaces utilized by MT vendors this information may become obsolete after that date without advance notice. Revision 1.0.
### 1.1 MT vendors described
This manual shows how to obtain APIs to the following MTs:

| MT name | Advantages | Disadvantages | Cost |
| ----------- | ----------- | ----------- | ----------- |
| Google Cloud Translation Basic (or Google Translate API v2)  | best-known vendor, numerous language pairs available  | quality differs per language pair, very complicated set-up  | paid service with a free quota |
| DeepL  |  very high quality, easy set-up  | limited number of language pairs  | paid service with a free trial |
| Amazon Translate (AWS)   |  numerous language pairs available | quality differs per language pair, complicated set-up  | paid service with a free quota |
| Modern MT   |  high-quality vendor, easy set-up | limited number of language pairs  | paid service with adaptive functions in a basic plan |

### 1.2 Privacy
More information on how the MT vendors listed in [Point 1.1](#11-mt-vendors-described) of this manual process your data is available from:

 - for DeepL:
 [https://www.deepl.com/pro-data-security/](https://www.deepl.com/pro-data-security/)
 - for Google Cloud Translation Basic (or Google Translate API v2):
 [https://cloud.google.com/translate/data-usage](https://cloud.google.com/translate/data-usage)
 - Amazon Translate (AWS):
 [https://docs.aws.amazon.com/translate/latest/dg/data-protection.html](https://docs.aws.amazon.com/translate/latest/dg/data-protection.html)
 - Modern MT:
 [https://www.modernmt.com/privacy/](https://www.modernmt.com/privacy/)

[2. How to set up Trados Studio 2021™ plugins](Trados.md)

[3. How to set up Memoq Translator Pro 9.8™ plugins](memoQ.md)

[4. How to obtain API keys for MT plugins](api_keys.md)

## 5. References
- [https://docs.memoq.com/current/en/Places/modernmt-settings.html](https://docs.memoq.com/current/en/Places/modernmt-settings.html), accessed on 29/09/2021
- [https://helpcenter.memoq.com/hc/en-us/articles/360019498179-How-to-set-up-the-DeepL-MT-plugin](https://helpcenter.memoq.com/hc/en-us/articles/360019498179-How-to-set-up-the-DeepL-MT-plugin), accessed on 27/09/2021
- [https://blog.api.rakuten.net/api-tutorial-google-translate-api/](https://blog.api.rakuten.net/api-tutorial-google-translate-api/), accessed on 28/09/2021
- [https://community.sdl.com/product-groups/translationproductivity/f/openexchange_applications/27164/deepl-plugin-not-working](https://community.sdl.com/product-groups/translationproductivity/f/openexchange_applications/27164/deepl-plugin-not-working), accessed on 25/09/2021
- [https://helpcenter.memoq.com/hc/en-us/articles/360010267380-Installing-Google-Translate-API-plugin-in-memoQ](https://helpcenter.memoq.com/hc/en-us/articles/360010267380-Installing-Google-Translate-API-plugin-in-memoQ), accessed on 29/09/2021
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
- [https://docs.memoq.com/ggl-tst/Places/mt-settings.html](https://docs.memoq.com/ggl-tst/Places/mt-settings.html), accessed on 29/09/2021 


