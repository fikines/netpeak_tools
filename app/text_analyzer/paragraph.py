from .utilities import clean_text


def get_paragraphs(text):
    text = text.strip()
    text = text.replace('\r\n','\n')
    text = text.replace('\n\n','\n')

    pg = text.split('\n')
  
    return pg

def get_count_of_paragraphs(paragraphs):
    return len(paragraphs)


def get_info_paragraphs(paragraphs):

    list_count_symbols = set()
    list_count_words = set()

    for paragraph in paragraphs:
        paragraph = clean_text(paragraph)
        list_count_symbols.add(len(paragraph))
        list_count_words.add(len(paragraph.split()))

    avg_symbols = round(sum(list(list_count_symbols))/len(list_count_symbols))

    avg_words = round(sum(list(list_count_words))/len(list_count_symbols))

    return [avg_symbols, avg_words]
