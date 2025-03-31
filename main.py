import sys
from stats import get_character_occurrences, get_num_words, get_sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    source_file = sys.argv[1]
    book_data = get_book_text(source_file)
    num_words = get_num_words(book_data)
    char_occurrences = get_character_occurrences(book_data)
    sorted_chars = get_sort_dictionary(char_occurrences)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {source_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char, occurence in sorted_chars.items():
        if char.isalpha():
            print(f"{char}: {occurence}")

    print("============ END ============")
if len(sys.argv) == 2:
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
