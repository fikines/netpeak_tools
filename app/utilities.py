from string import punctuation
import re


def clean_text(original_text):
   
    clean_text = re.sub(r'[^A-zА-я0-9]', ' ', original_text)
    return clean_text