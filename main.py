from stats import *
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]
print(f"Processing oook: {path_to_book}")

def main():
    print(f"Debug: Processing book at path: {path_to_book}")
    print(f"""============ BOOKBOT ============
Analyzing book found at {path_to_book}...""")
    print("----------- Word Count ----------")
    word_count = get_num_words(path_to_book)
    print(f"Debug: Word count result: {word_count}")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_sorted(path_to_book)
    print("============= END ===============")


main()
"""



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

"""