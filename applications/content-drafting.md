Machine translation allows to quickly draft content in natural language. 

# Use cases:


### Mock-up localisation
Raw machine-translated text is a good mock-up to verify how the target language appears in localised content such as:
* web pages
* user interface
* images and diagrams.

Machine translation produces natural-language content that shall not be verified for accuracy at this step, but presents such features as target alphabet and typical word lenth or sentence length. 
When applied to localised content, MT allows to quickly detect localisation issues, for example:
* National characters are corrupted or missing.
* Words or phrases are truncated due to lack of screen space.
* Sort order is not appropriate for the target language.

Detecting these issues at an early phase allows taking corrective actions, in parallel with the actual professional translation or  [post-editing](post-editing.md), or planning for necessary post-processing of localised content, for example:
* Enable proper locale, character sets and fonts.
* Resize assets to allow for text of various length, or plan time and effort for resizing the assets when the content will be translate.
* Enable sorting in the target locales.

<!-- example of mock-up UI localisation with national characters corrupted -->

<!-- example of mock-up image localisation with text truncated -->

In the following example, source (English) image relies on the exact length of English text: 

![English image](./_images/image_with_text_eng.svg)

Localised images will have texts of a different length depending on the language, e.g. German text is usually longer and does not fit, so some work will be needed after the translation to adjust the localised images:

![German image](./_images/image_with_text_ger.svg)

<!-- example of mock-up UI localisation with wrong sorting of a translated list -->


# Writing aid
Authors can use machine translation to draft a text in foreign languge which they know but can use some help with typical expressions and appropriate phrases. 
First they write paragraphs in their native language and then edit the machine output for accuracy (conveying the message), terminology and consistency. 

This technique avoids the basic difficulty of post-editing where a translator needs to first understand the source, because the author knows exactly what they want to communicate. 

<!-- example of drafting text in DeepL -->

In this example, DeepL in browser is used to draft a paragraph of English text from Polish source:

![Drafting text in DeepL](./_images/drafting-text-deepl.png)