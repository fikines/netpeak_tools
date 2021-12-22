
def get_number_of_symbols(text, original_text):

    """
    Get Text 
    Clean empty symbols
    Get number of symbols
    Return number of symbols in text
    """
    clean_text = text

    number_of_symbols_with_empty = len(original_text)

    clean_text = clean_text.replace(' ', "")

    number_of_symbols = len(clean_text)

    return number_of_symbols_with_empty, number_of_symbols