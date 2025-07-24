from stats import count_words, count_characters


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    words_count = count_words(book_text)
    chars_count = count_characters(book_text)
    print(f"{words_count} words found in the document")
    print(chars_count)


main()

