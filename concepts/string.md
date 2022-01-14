---
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

In software, every character has a unique number.

The computer does not know what letters are, only numbers.
So every character needs to be represented by a unique number (codepoint).

For example, the **ASCII** standard maps English and other particularly useful characters to numbers.

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

In the early days of the internet, multiple standards evolved to represent text content in more languages.  In the 2000s, the **UTF-8** standard became the most popular encoding on the internet.

The most common problem is when text is encoded with one standard, but decoded with another.  The result is often unreadable.

> Example of an encoding problem
> The text  
> > `A man with a telescope 🔭 from the city of Třebíč`
>
> When encoded to UTF-8 and decoded from a Windows encoding  
> > `A man with a telescope ð­ from the city of TÅebÃ­Ä`

This problem often happens at the interfaces between different components or systems.
