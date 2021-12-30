---
description: String
---

# String

A string is a sequence of characters.
In computer programming, strings are used to represent text.

By default, a string is _plain text_.
It does not represent rich formatting or styles, like font-size and color.

- A string with no characters is the _empty string_.
- A string can contain even just a single character: `a`
- A string can contain any character even outside the English alphabet, including emojis: `A man with a telescope 🔭 from the city of Třebíč`
- A string can be very long (like paragraphs, books) and can contain control characters like _newline_:
   ```
   Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
   
   Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
   ```

## Encoding

A particular focus is paid to how the characters are encoded in the string.
The computer does not know what letters are, only numbers.
Therefore every character needs to have some number assigned (codepoint).

### ASCII

The ASCII standard is a widely popular codetable that maps English and other particularly useful characters to numbers.

| Character | Decimal representation |
| ... | ... |
| `A` | 65 |
| `B` | 66 |
| `C` | 67 |
| ... | ... |

Note that the computer distinguishes between lowercase `a` and uppercase `A`.
These two characters are different and have different codes assigned to them. 

### Other encodings

The ASCII standard unfortunately covers only 128 characters which is not sufficient for modern usage across multiple languages many with their own alphabet versions.
Multiple solutions were proposed that extended ASCII, the most popular ones are Unicode and Windows encoding.
Among researchers, the UTF8 (a technical specification of Unicode) is the most popular though Windows-based user computers use the later encoding.

The biggest issue is when the text is encoded in one way but the computer tries to interpret it as if it was stored with a different encoding.
The resulting text is then filled with seemingly-random letters.
If the third example was stored as UTF8 and then interpreted with a specific Windows encoding, it would look as `A man with a telescope ð­ from the city of TÅebÃ­Ä`.

The modern software stacks are sometimes very large and it takes only one of them to expect a different encoding to cause further errors.