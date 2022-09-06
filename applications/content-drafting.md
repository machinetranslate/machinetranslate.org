Machine translation allows to quickly draft content in natural language. Applications:


# Mock-up localization
Raw machine-translated text is a good mock-up to verify how the target language appears in localized content such as:
* user interface,
* images and diagrams.

MT produces natural-language content that shall not be verified for accuracy at this step, but presents such features as target alphabet and typical word/sentence length. 
When applied to localized content, MT allows to quickly issues, for example:
* national characters corrupted or missing,
* words or phrases truncated due to lack of screen space,
* wrong sort order.
Detecting these issues at early phase allows taking corrective actions, in parallel with the actual professional translation or post-editing, or planning for necessary post-processing of localized content, for example:
* enable more character sets in localization (locale, font, etc.)
* resize assets, or plan time and effort for resizing the assets with translated content,
* enable sorting in the target locales.

<!-- example of mock-up UI localization with national characters corrupted -->

<!-- example of mock-up image localization with text truncated -->

In the following example, source (English) image relies on the exact length of English text: 

![English image](./_images/image_with_text_eng.svg)

Localized images will have texts of a different length depending on the language, e.g. German text is usually longer and does not fit, so some work will be needed after the translation to adjust the localized images:

![German image](./_images/image_with_text_ger.svg)

<!-- example of mock-up UI localization with wrong sorting of a translated list -->


# Writing aid
One can write fluently in their native language and use MT to draft text in the target language which they understand but need some help with correct expressions and phrases. 
This technique avoids the basic difficulty of post-editing where a translator needs to first understand the source, because the author knows exactly what they want to communicate. 
After writing down the message in their native language, the author needs to review the MT for accuracy (conveying the message), proper terminology and consistency.

<!-- example of drafting text in DeepL -->

In this example, DeepL in browser is used to draft a paragraph of English text from Polish source:

![Drafting text in DeepL](./_images/drafting-text-deepl.png)