
def main():
    with open ("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents 

def word_count():
    file_contents = main()
    words = file_contents.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def character_count():
    file_contents = main()
    lowercase_string = file_contents.lower()
    character_dictionary = {}
    for char in lowercase_string:
        if char in character_dictionary: 
            character_dictionary[char] += 1
        else:
            character_dictionary[char] = 1
    return character_dictionary

def alpha():
    char_dictionary = character_count()
    alpha_dictionary = {}
    for char in char_dictionary:
        if char.isalpha() == True:
            alpha_dictionary[char] = char_dictionary[char]
    return alpha_dictionary

def alpha_report():
    alpha_dict = alpha()
    alpha_list = []
    for character in alpha_dict:
        alpha_list.append(f"The '{character}' was found {alpha_dict[character]} times")
    return alpha_list

def report():
    report_briefing = "--- Begin report of books/frankenstein.txt ---"
    count = f"{word_count()} words found in the document"
    alpha_list = alpha_report()
    end_report = "--- End report ---"
    return report_briefing, count, alpha_list, end_report

print(report())