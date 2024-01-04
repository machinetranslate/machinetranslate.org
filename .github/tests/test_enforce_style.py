import re

import enchant
import spacy

from .find_missing_links import walk_directory


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
                    # Skip words that have the same spelling in both US and UK English or are wrong for both
                    if ((us.check(raw_word) == uk.check(raw_word)) or (uk.check(raw_word) and not us.check(raw_word))):
                        continue
                    # Skip CamelCase and all-uppercase words
                    if is_camel_case(raw_word) or raw_word.isupper():
                        continue
                    # Check if the word is a proper noun in context
                    assert is_proper_noun_in_context(_line, raw_word), \
                        f'US-specific spelling: "{raw_word}" in {file_path} \n\n\t at the line: {line} \n\n\tsuggestions: {uk.suggest(raw_word)} \n'


EXCLUDE_DIRS = ['vendor']
EXCLUDE_FILES = ['README.md', 'CHANGELOG.md']
DIR = ('../../')

def test_main():
    article_paths = list(walk_directory(DIR, exclude_dirs=EXCLUDE_DIRS, exclude_files=EXCLUDE_FILES))
    for article_path in article_paths:
        check_spellings(article_path)
