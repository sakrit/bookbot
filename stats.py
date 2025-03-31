def get_num_words(data):
    word_count = len(data.split())
    return word_count

def get_character_occurrences(text_data):
    char_dict = {}
    for text in text_data:
        text_to_lower = text.lower()
        if text_to_lower in char_dict:
            char_dict[text_to_lower] += 1
        else:
            char_dict[text_to_lower] = 1
    return char_dict

def get_sort_dictionary(dictionary):
    items = list(dictionary.items())
    items.sort(key=lambda item: item[1], reverse=True)
    return dict(items)
