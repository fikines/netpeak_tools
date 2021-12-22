from string import punctuation

PUNCTUATION = set(punctuation)

def clean_text(original_text):
    """
    Get Text 
    Clean text from punctuation and empty symbols
    Get number of symbols
    """
    clean_text = original_text
    PUNCTUATION.add('–')
    PUNCTUATION.add('⅓')
    PUNCTUATION.add('в…“')
    PUNCTUATION.add('в…')
    for ele in clean_text:
        if ele in PUNCTUATION:
            clean_text = clean_text.replace(ele, " ")

    clean_text = clean_text.replace('\n', " ")
    clean_text = clean_text.replace('  ', " ")
    return clean_text