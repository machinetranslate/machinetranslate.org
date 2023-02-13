---
parent: Customisation
title: Crawling
description: Crawling the web for machine translation training data
---

Web **crawling** is the process of automatically collecting large amounts of [training data](/customisation/training-data.md) for [language models](/concepts/language-model.md) and machine translation systems.
Crawling is used to acquire [parallel data](/customisation/parallel-data.md) by visiting bilingual or multilingual websites and extracting parallel text sets.
Another approach is to use web crawling to collect monolingual text in a target language.

### Process

1. Visiting the first URL, manually specified by the user or selected from a pre-defined list of URLs
2. Extracting URLs from the visited web page and adding them to a queue of URLs to be visited
3. Extracting text data from the visited web page and storing it in a database for later use
4. URL filtering to determine which URLs to visit next based on the pre-defined criteria
5. Repetition of URL extraction, text extraction, and URL filtering for each URL in the queue
6. Preprocessing and [filtering](/customisation/filtering.md) of the extracted text data to remove noise and normalise quality

For parallel data collection, the crawler also uses [language identification](/customisation/language-identification.md) to extract multilingual text data from the same website.

### Challenges

The web-crawled content is often noisy and contains irrelevant information, inconsistent formatting, and errors.
The extracted and preprocessed data should undergo evaluation before processing.

Crawling can also raise privacy and ethical concerns if the web crawlers overstep website privacy policies and terms of use.
