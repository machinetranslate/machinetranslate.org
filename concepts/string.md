---
grand_parent: Resources
parent: Concepts
title: String
description: A sequence of characters
---

A string is a sequence of characters.
In computer programming, strings are used to represent text.

By default, a string is _plain text_.
It does not represent rich formatting or styles, like font size and color.

- A string with no characters is the _empty string_.
- A string can contain even just a single character: `a`
- A string can contain any character even outside the English alphabet, including emojis: `A man with a telescope 🔭 from the city of Třebíč`
- A string can be very long and can contain control characters like _newline_:

   ```
   Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

   Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
   ```
So a string can even be used for a paragraph or book.

## Encoding

Computers deal with numbers, not with characters.  In order to represent a character, it has to be encoded into a series of bits.  Since computers deal with bytes (8 bits), a character is typically encoded into one or several bytes of data.

First, one has to decide how many characters we care to represent.   That's what is called the **character set**.   Each characted is typically assigned a **codepoint**.
Then, one has to decide how to encode these characters, i.e. which byte values to assign for that codepoint.

A character set can have one or several possible encodings. 

The **ASCII** standard defines 128 characters and a single encoding.  Here is an example of a few ASCII characters and their decimal byte values:

| Character | Decimal representation |
| ... | ... |
| `A` | 65 |
| `B` | 66 |
| `C` | 67 |
| ... | ... |

⚠️ Lowercase `a` and uppercase `A` are two different characters.

ASCII only has 128 characters.
- numeric digits
- the letters of the Latin alphabet required for basic English
- common punctuation characters
- control characters

ASCII cannot represent `β`, `喂`, or even `é`.

As the computer world became more international, a better character set quickly became necessary. Early attempts consisted in extending ASCII to multiple code pages, with each codepage being able to represent a group of characters used in a given set of languages.  That started with DOS, and continued with Windows 3.x and future versions. But that was poorly interchangeable, as the same byte values could represent different characters depending on which codepage was used.

In 1991, a new standard emerged called Unicode.  Its goal was to represent as many characters as possible in a single character set and solve the interoperability issue. Its first version contained over 7000 characters.  As of September 2022, Unicode is in version 15.0 and contains 149,186 characters or codepoints!

Unicode has many different encodings. The most common one is **UTF-8**, but other exist like **UTF-16** or even **UTF-32**.  UTF-8 is a variable length encoding, while UTF-32 is fixed length (as long as the character set doesnt try to represent more than 4 billion chars!). UTF-32 is a memory hog, but it is predictable since it's fixed length and it has the advantage that the byte values are an exact match to the codepoint value.  UTF-16 is also variable length, not fixed length, a mistake often made by newbie developers.  In UTF-16, in order to represent characters beyond the first plane of Unicode (Basic Multilingual plane), the encoding uses **surrogate pairs**.  Don't ever assume that a character is always encoded with 2 bytes in UTF-16!

A common problem is that legacy character sets and their encodings are still supported by many operating systems (for compatibility reasons with old software), while newer systems may use a Unicode encoding. When text is encoded with one standard, but decoded with another, the result is often unreadable.

> Example of an encoding problem
> The text  
> > `A man with a telescope 🔭 from the city of Třebíč`
>
> When encoded to UTF-8 and decoded from a Windows encoding  
> > `A man with a telescope ð­ from the city of TÅebÃ­Ä`

This problem often happens at the interfaces between different components or systems.
