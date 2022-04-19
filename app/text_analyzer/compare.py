    
def sort_dict(words_dict):
    words_dict = sorted(words_dict.items(), key=lambda x:x[1][0], reverse = True)
    sortdict = dict(words_dict)
    return sortdict


def words_difference(info_main, info_comp):
    
    words_1 = set()
    for key in info_main['words']['sem core']:
        words_1.add(key)
    
    words_2 = set()
    for key in info_comp['words']['sem core']:
        words_2.add(key)    
   
    words = words_1.difference(words_2)
    data = dict()

    for key in words:
        number = len(info_main['words']['all words'][key])
        percent = round((number/(info_main['statistics']['number of words'])*100),2)
        data[key] = [number,percent]

    data = sort_dict(data)

    return data


def words_common(info_main, info_comp):
    words_1 = set()
    for key in info_main['words']['sem core']:
        words_1.add(key)
    
    words_2 = set()
    for key in info_comp['words']['sem core']:
        words_2.add(key)
    
    words = words_1.intersection(words_2)
    data = dict()

    for key in words:
        number_1 = len(info_main['words']['all words'][key])
        percent_1 = round(((number_1/info_main['statistics']['number of words'])*100),2)
        number_2 = len(info_comp['words']['all words'][key])
        percent_2 = round(((number_2/info_comp['statistics']['number of words'])*100),2)
        data[key] = [number_1, percent_1, number_2, percent_2]

    return data