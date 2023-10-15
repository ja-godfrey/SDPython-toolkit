"""
Text Cleaning Example Module
----------------------------

This module provides illustrative examples of how to use various text cleaning utility functions defined in 
the `text_cleaning.py` module. These examples are meant to serve as a basic guide on how to utilize each 
function and its parameters effectively for different text cleaning scenarios.

Note: For comprehensive documentation and parameter details of each function, refer to the docstrings in 
`./../text_cleaning.py`.

Author: [Your Name]
Date: [Creation Date]
Version: 1.0
"""

text = "The cost is 100 dollars"
print(remove_numbers(text))
# Expected Output: "The cost is  dollars"

text = "NASA was formed in USA"
acronyms_dict = {"NASA": "National Aeronautics and Space Administration", "USA": "United States of America"}
print(replace_acronyms(text, acronyms_dict))
# Expected Output: "National Aeronautics and Space Administration was formed in United States of America"

text = "I am soooo happy!!"
print(remove_repeated_characters(text, threshold=2))
# Expected Output: "I am soo happy!!"

text = "It's a beautiful day, isn't it?"
contractions_dict = {"It's": "It is", "isn't": "is not"}
print(expand_contractions(text, contractions_dict))
# Expected Output: "It is a beautiful day, is not it?"

text = "This is amazing 😃🎉"
print(remove_emoji(text))
# Expected Output: "This is amazing "

text = "btw, that was awesome lol"
slang_dict = {"btw": "by the way", "lol": "laugh out loud"}
print(replace_slang(text, slang_dict))
# Expected Output: "by the way, that was awesome laugh out loud"

text = "Love #Python and #DataScience"
print(extract_hashtags(text))
# Expected Output: ['#Python', '#DataScience']

text = "Visit us at https://example.com"
print(remove_URLs(text))
# Expected Output: "Visit us at "

text = "For inquiries, contact us at info@example.com"
print(remove_email_addresses(text))
# Expected Output: "For inquiries, contact us at "

text = "I have 2 apples"
print(convert_numbers_to_words(text))
# Expected Output: "I have two apples"
