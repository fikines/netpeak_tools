from requests_html import HTMLSession


def get_words(text):
    """
    Return number of words in text
    """
    return text.split()
    

def get_number_of_words(words):
    """
    Return number of words in text
    """
    return len(words)


def check_for_correct(answer):

    if answer.split()[-1] == '-':
        return True
    else:
        return False


def check_word_type(answer):

    types = ['числително','съществително','прилагателно','глагол','местоимение','наречие']

    if sum(x in str(answer) for x in types) > 0:
        return True
    else:
        return False

   
def clean_answer(answer):

    arr = []
    for row in str(answer).split('\n'):
        if not str(row).startswith(' ') and len(str(row)) != 0:
            arr.append(row)
            
    return arr

    
def sort_dict(words_dict):
    words_dict = sorted(words_dict.items(), key=lambda x:x[1][1], reverse = True)
    sortdict = dict(words_dict)
    return sortdict


def get_frequency(all_words, words):

    data = dict()

    for key in words:
        number = len(all_words[key])
        per_cent = round((number/len(all_words)*100),2)
        data[key] = [words[key],number,per_cent]
    data = sort_dict(data)
    return data
    

def get_words_info(words):

    incorrect_words = dict()
    sem_core = dict()
    dict_words = dict()

    text = ''
    words = [x.lower() for x in words]

    arr = [words[d:d+100] for d in range(0, len(words), 100)]
    for row in arr:

        line = ', '.join(row)

        url = f'http://slovored.com/search/grammar/{line}'

        with HTMLSession() as session:
            resp = session.get(url)

        try:
            answers = resp.html.xpath('//div[@class="result"]/pre/text()')
        except Exception as e:
            print (f'[ERROR] {e}')
            return False

        text += ' '.join(answers)

    cleaned_answers = clean_answer(answer= text)

    for answer in cleaned_answers:

        word = answer.split(' ')[0]

        if len(word) < 3:
            continue

        if  check_for_correct(answer):

            if word in incorrect_words: 
                incorrect_words[word].add(word)
            else:
                incorrect_words[word] = {word}
            
            if word in dict_words: 
                dict_words[word].append(word)
            else:
                dict_words[word] = [word]

        elif  check_word_type(answer= answer):
            general_form = answer.split(' ')[-1]

            if general_form in sem_core: 
                sem_core[general_form].add(word)
            else:
                sem_core[general_form] = {word}

            if general_form in dict_words: 
                dict_words[general_form].append(word)
            else:
                dict_words[general_form] = [word]
        
        else:
            if word in dict_words: 
                dict_words[word].append(word)
            else:
                dict_words[word] = [word]

    sem_core = get_frequency(dict_words, sem_core)
    incorrect_words = get_frequency(dict_words, incorrect_words)

    GENERAL_DATA = {
        'all words': dict_words,
        'incorrect words': incorrect_words,
        'sem core': sem_core
    }
  
    return GENERAL_DATA
    
    