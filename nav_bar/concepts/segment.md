---
nav_exclude: true
parent: Concepts
title: Segment
community_search_term: "segments"
description: A sequence of characters
---

A **segment** is a unit in a document or other files processed by a computer-aided translation (CAT) tool.

Segment content depends on the type of translated content:

- In a document, a segment is usually a sentence or an equivalent to a sentence.
- In a spreadsheet, a segment is a cell.
- In user interface resource files, a segment can be a menu option, a text on a button, a field label, an error message text, etc.

Segment is equivalent to a [string](string.md). However, a segment can either be plain text or can also include [tags or placeholders](/applications/advanced-concepts/tags-and-placeholders.md).

Segments coupled into source-target pairs are called translation units. Translation units are building blocks of a translation memory.
Splitting text into segments allows to apply matches from translation memory and to identify repetitions in an input text.
