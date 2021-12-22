from utilities import clean_text
from string import punctuation
import nltk

PUNCTUATION = set(punctuation)


def get_sentences(text):

    sent_text = nltk.sent_tokenize(text)
    # pprint(sentences)
    return sent_text


def get_count_of_sentences(sentences):
    # pprint(sentences)
    return len(sentences)


def info_sentences(sentences):

    list_count_symbols = set()
    list_count_words = set()

    for sentence in sentences:
        sentence = clean_text(sentence)
        list_count_symbols.add(len(sentence))
        list_count_words.add(len(sentence.split()))

    avg_symbols = round(sum(list(list_count_symbols))/len(list_count_symbols))

    avg_words = round(sum(list(list_count_words))/len(list_count_symbols))

    return [avg_symbols, avg_words]

