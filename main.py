import sys
from stats import count_words, count_characters, dict_to_list_of_dicts


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def print_letters_and_count(list_of_dicts):
    for dict in list_of_dicts:
        print(f"{dict["char"]}: {dict["count"]}")
    return 0


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    words_count = count_words(book_text)
    chars_count = count_characters(book_text)
    list_of_dicts = dict_to_list_of_dicts(chars_count)

    # PRINT REPORT - BEGIN
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print(f"----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    print_letters_and_count(list_of_dicts)
    print("============= END ===============")

main()

