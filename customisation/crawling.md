---
parent: Customisation
title: Crawling
description: Crawling the web for machine translation training data
---

**Crawling** or **web scraping** is the process of automatically collecting large amounts of [training data](/customisation/training-data.md) for [language models](/concepts/language-model.md) and machine translation systems.

Bilingual or multilingual websites provide text sets for [parallel data](/customisation/parallel-data.md) extraction.
Web crawling also collects monolingual text in the target language.

### Process

1. Visit the first URL, manually specified by the user or selected from a pre-defined list of URLs
2. Extract URLs from the visited web page and add them to a queue of URLs to be visited
3. Extract text data from the visited web page and store it in a database for later use
4. Filter URLs to determine which web pages to visit next based on the pre-defined criteria
5. Repeat the steps of URL extraction, text extraction, and URL filtering for each URL in the queue
6. Preprocess and [filter](/customisation/filtering.md) the extracted text data to remove noise and normalise quality

For parallel data collection, the crawler also uses [language identification](/customisation/language-identification.md) to extract multilingual text data from the same website.

### Challenges

The web-crawled content is often noisy and contains irrelevant information, inconsistent formatting, and errors.
The extracted and preprocessed data should undergo evaluation before processing.

Crawling can also raise privacy and ethical concerns if the web crawlers overstep website privacy policies and terms of use.
