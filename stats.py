def get_word_count(text):
    return len(text.split())
def get_character_count(text):
    text = text.lower()
    char_dict = {}
    l_chars = list(text)
    for char in l_chars:
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1
    return char_dict

def sorted_list_of_dicts(char_dict):
    temp_list = []
    for key, value in char_dict.items():
        temp_list.append({'character': key, 'count': value})
    return sorted(temp_list, key=lambda x: x['count'], reverse=True)