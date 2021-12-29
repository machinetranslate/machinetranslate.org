---
description: String
---

# String

A string is an object in memory that stores a sequence of characters and colloquially it is the representation of text in the computer.
Examples:
1. `bicycle`
2. `A man with a telescope 🔭 from the city of Třebíč`
3. ```
   Introduction: Lorem Ipsum is simply dummy text of the printing and typesetting industry.
   
   Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
   ```

The first example is simply a 7-letter word of English letters.
The second example shows that a string can contain spaces, letters from non-English alphabets and even emojis.
The last example demonstrates that even paragraphs with special whitespace characters, such as the newline, usually written as `\n` are stored as a string.

## Encoding

A particular focus is paid to how the characters are encoded in the string.
The computer does not know what letters are, only numbers.
Therefore every character needs to have some number assigned (codepoint).

The ASCII standard is a widely popular codetable that maps English and other particularly useful characters to numbers.
It unfortunately covers only 128 characters which is not sufficient for modern usage across multiple languages many with their own alphabet versions.
Multiple solutions were proposed that extended ASCII, the most popular ones are Unicode and Windows encoding.
Among researchers, the UTF8 (a technical specification of Unicode) is the most popular though Windows-based user computers use the later encoding.

The biggest issue is when the text is encoded in one way but the computer tries to interpret it as if it was stored with a different encoding.
The resulting text is then filled with seemingly-random letters.
If the second example was stored as UTF8 and then interpreted with a specific Windows encoding, it would look as `A man with a telescope ð­ from the city of TÅebÃ­Ä`.

The modern software stacks are sometimes very large and it takes only one of them to expect a different encoding to cause further errors. 