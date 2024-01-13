import re

import enchant
import spacy

from .find_missing_links import walk_directory

# Checks that we use UK spellings for words that differ between the UK and US
# Permits US spellings for proper nouns.

# Load the English language model for Spacy
NLP = spacy.load("en_core_web_sm")

# Check if a token in a Spacy document is a proper noun
def is_proper_noun_in_context(line, word):
    doc = NLP(line)
    for token in doc:
        if token.text == word and token.pos_ == 'PROPN':
            return True
    return False

def is_camel_case(word):
    return any(c.isupper() for c in word[1:])

def check_spellings(file_path):
    # Create dictionaries for US and UK English
    us = enchant.Dict("en_US")
    uk = enchant.Dict('en_GB')

    with open(file_path, 'r', encoding='utf-8') as f:
        # Skip first line
        f.seek(0)
        next(f)
        is_frontmatter = True
        in_html_block = False

        for line in f:
            # Skip if frontmatter
            if is_frontmatter:
                if line.startswith('---'):
                    is_frontmatter = False
                continue
            # Skip HTML
            if '<' in line and '>' in line:
                in_html_block = True

            if in_html_block:
                continue

            _line = line
            # Remove existing Markdown links and Liquid tags
            _line = re.sub(r'\[(.*?)\]\([^)]*?\)|\{\{[^}]*\}\}|{%[^\n]*%}', ' ... ', _line)

            for word in _line.split():
                # Extract only the letters
                raw_word = re.sub(r'^[^a-zA-Z\'-]*|[^a-zA-Z\'-]*$', '', word)

                if raw_word:
                    
                    # Skip CamelCase and all-uppercase words
                    if is_camel_case(raw_word) or raw_word.isupper():
                        continue

                    # If a US word but not a UK word
                    if us.check(raw_word) and not uk.check(raw_word)
                    
                        # Check if the word is a proper noun in context
                        # This is a relatively expensive check.
                        assert is_proper_noun_in_context(_line, raw_word), f'''US-specific spelling: 
                                "{ raw_word }" in { file_path }
                                    line: { line }
                                    suggestions: { uk.suggest(raw_word) }
                             '''

EXCLUDE_DIRS = ['vendor']
EXCLUDE_FILES = ['README.md', 'CHANGELOG.md']
DIR = ('../../')

def test_main():
    article_paths = list(walk_directory(DIR, exclude_dirs=EXCLUDE_DIRS, exclude_files=EXCLUDE_FILES))
    for article_path in article_paths:
        check_spellings(article_path)
