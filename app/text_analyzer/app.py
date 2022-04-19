from .symbols import get_number_of_symbols
from .words import get_words, get_words_info, get_number_of_words
from .sentence import get_count_of_sentences,get_sentences, info_sentences
from .paragraph import get_info_paragraphs, get_paragraphs, get_count_of_paragraphs
from .compare import words_difference,words_common
from .utilities import clean_text


def get_info(text):
    cleaned_text = clean_text(text)
    list_of_words = get_words(cleaned_text)
    list_of_sentences = get_sentences(text)
    list_of_paragraphs = get_paragraphs(text)

    symbols_of_text = get_number_of_symbols(cleaned_text, text)
    sentence_info = info_sentences(list_of_sentences)
    number_of_sentences = get_count_of_sentences(list_of_sentences)

    number_of_paragraphs = get_count_of_paragraphs(list_of_paragraphs)
    paragraphs_info = get_info_paragraphs(list_of_paragraphs)

    number_of_words =  get_number_of_words(list_of_words)
    words_info = get_words_info(list_of_words)

    number_of_incorrect = len(words_info['incorrect words'])

    data ={
        'statistics':{
            'count of symbols':symbols_of_text[0],
            'count of symbols(- empty)':symbols_of_text[1],
            'number of sentences': number_of_sentences,
            'symbols in sentences': sentence_info[0],
            'words in sentences': sentence_info[1],
            'number of paragraphs': number_of_paragraphs,
            'symbols in paragraphs': paragraphs_info[0],
            'words in paragraphs': paragraphs_info[1],
            'number of words': number_of_words,
            'number of unknown': number_of_incorrect 
            },
        'words': words_info 
    }
    
    return data


def collecting(main_text, competitor_text):
    info_text_main = get_info(main_text)
    info_text_comp = get_info(competitor_text)
    diffence_main_comp = words_difference(info_main= info_text_main, info_comp= info_text_comp)
    diffence_comp_main = words_difference(info_main= info_text_comp, info_comp= info_text_main)
    common = words_common(info_main= info_text_main, info_comp= info_text_comp)

    general_data = {
        'data main text': info_text_main['statistics'],
        'data comp text': info_text_comp['statistics'],
        'words':{
            'main words': info_text_main['words'] ,
            'comp words': info_text_comp['words'] ,
            'difference main & comp': diffence_main_comp,
            'difference comp & main': diffence_comp_main,
            'common words': common
        }
    }
    return [main_text,competitor_text, general_data]

