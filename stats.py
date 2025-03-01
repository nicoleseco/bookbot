import sys


def get_book_text(path_to_book):
    try:
        with open (path_to_book) as f:
            file_contents = f.read()
            print(f"Successfully read {len(file_contents)} characters from {path_to_book}")
            return file_contents 
    except Exception as e:
        print(f"Error reading {path_to_book}: {e}")
        return ""

def get_num_words(path_to_book):
    file_contents = get_book_text(path_to_book)
    words = file_contents.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def character_count(path_to_book):
    file_contents = get_book_text(path_to_book)
    lowercase_string = file_contents.lower()
    character_dictionary = {}
    for char in lowercase_string:
        if char in character_dictionary: 
            character_dictionary[char] += 1
        else:
            character_dictionary[char] = 1
    return character_dictionary

def alpha(path_to_book):
    char_dictionary = character_count(path_to_book)
    alpha_dictionary = {}
    for char in char_dictionary:
        if char.isalpha() == True:
            alpha_dictionary[char] = char_dictionary[char]
    return alpha_dictionary



def alpha_dicts_from_dict(alpha_dict):
    dict_list= []
    for char, count in alpha_dict.items():    
        dict_list.append({"char": char, "count": count})
    return dict_list


def sort_on(dict):
    return dict["count"]
    
def sorted_list(alpha_dict):
    alpha_char_list = alpha_dicts_from_dict(alpha_dict)
    alpha_char_list.sort(reverse=True, key=sort_on)
    return alpha_char_list 

def print_sorted(path):
    alpha_dict = alpha(path)
    sorted_chars = sorted_list(alpha_dict)
    for item in sorted_chars:
        char = item["char"]
        count = item["count"]
        print(f"{char}: {count}")