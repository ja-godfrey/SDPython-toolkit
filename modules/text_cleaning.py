"""
Text Cleaning Utilities
------------------------

This module provides a collection of utility functions specifically tailored for cleaning and preprocessing textual data. 
These functions address common challenges faced in natural language processing tasks, including but not limited to:
- Removing numbers, URLs, and email addresses
- Expanding contractions and acronyms
- Handling repeated characters and slang terms
- Extracting specific elements like hashtags

By using these tools, users can simplify and standardize the initial stages of text data preprocessing before further analysis or modeling.

Usage:
    from text_cleaning import remove_numbers, remove_emoji, expand_contractions, ...

Note: Some functions might require dictionaries for acronyms, contractions, or slang terms replacement. Ensure they are provided as needed.

Author: Jason Godfrey
Date: 10/13/2023
Version: 1.0
"""


import re
from word2number import w2n 

def remove_numbers(text):
    """
    Removes all numeric characters from a text.

    Parameters:
        text (str): The input text.

    Returns:
        str: The text with all numeric characters removed.
    """
    return re.sub(r'\d+', '', text)

def replace_acronyms(text, acronyms_dict):
    """
    Replaces acronyms/abbreviations in a text with their full forms 
    based on a provided dictionary.

    Parameters:
        text (str): The input text.
        acronyms_dict (dict): Dictionary with acronyms as keys and full forms as values.

    Returns:
        str: The text with acronyms replaced.
    """
    words = text.split()
    replaced_words = [acronyms_dict[word] if word in acronyms_dict else word for word in words]
    return ' '.join(replaced_words)

def remove_repeated_characters(text, threshold=2):
    """
    Removes characters that are repeated more than a specified threshold.

    Parameters:
        text (str): The input text.
        threshold (int): The maximum allowed consecutive repeating characters.

    Returns:
        str: The text with excess characters removed.
    """
    return re.sub(r'(.)\1{'+str(threshold-1)+',}', r'\1'*threshold, text)

def expand_contractions(text, contractions_dict):
    """
    Expands contractions based on a provided dictionary.

    Parameters:
        text (str): The input text.
        contractions_dict (dict): Dictionary with contractions as keys and expanded forms as values.

    Returns:
        str: The text with contractions expanded.
    """
    words = text.split()
    expanded_words = [contractions_dict[word] if word in contractions_dict else word for word in words]
    return ' '.join(expanded_words)

def remove_emoji(text):
    """
    Strips emojis from a text string.

    Parameters:
        text (str): The input text.

    Returns:
        str: The text without emojis.
    """
    # A wide range of unicode codes is used to define emojis. 
    # The below pattern should cover most cases.
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def replace_slang(text, slang_dict):
    """
    Replaces slang terms or colloquial expressions with their standard forms
    based on a provided dictionary.

    Parameters:
        text (str): The input text.
        slang_dict (dict): Dictionary with slang as keys and standard forms as values.

    Returns:
        str: The text with slang replaced.
    """
    words = text.split()
    replaced_words = [slang_dict[word] if word in slang_dict else word for word in words]
    return ' '.join(replaced_words)

def extract_hashtags(text):
    """
    Extracts and returns all hashtags from a text.

    Parameters:
        text (str): The input text.

    Returns:
        list: A list of extracted hashtags.
    """
    return re.findall(r'#\w+', text)

def remove_URLs(text):
    """
    Removes URLs from a text.

    Parameters:
        text (str): The input text.

    Returns:
        str: The text without URLs.
    """
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    return url_pattern.sub('', text)

def remove_email_addresses(text):
    """
    Removes email addresses from a text.

    Parameters:
        text (str): The input text.

    Returns:
        str: The text without email addresses.
    """
    email_pattern = re.compile(r'\S+@\S+')
    return email_pattern.sub('', text)

def convert_numbers_to_words(text):
    """
    Converts numeric characters to their word equivalents 
    (e.g., "3" to "three").

    Parameters:
        text (str): The input text.

    Returns:
        str: The text with numeric characters converted to words.
    """
    words = text.split()
    converted_words = []
    for word in words:
        if word.isnumeric():
            try:
                word_as_num = w2n.word_to_num(word)
                converted_words.append(word_as_num)
            except ValueError:
                converted_words.append(word)
        else:
            converted_words.append(word)
    return ' '.join(converted_words)
