def count_words(book_text):
    return len(book_text.split())


def count_characters(book_text):
    chars = {}
    for c in book_text:
        c = c.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


def dict_to_list_of_dicts(chars_dict):
    list_of_dicts = []
    for k, v in chars_dict.items():
        list_of_dicts.append({"char": k, "count": v})
    sortedlist = sorted(list_of_dicts, key=lambda x: x["count"], reverse=True)
    return sortedlist
