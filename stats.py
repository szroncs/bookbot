def get_num_words(book_content):
    words = book_content.split()
    return len(words)


# takes a string, and returns a dictionary key=char value=int of times each character appears
# convert all chars to lowercase
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_chars_dict(chars):
    sorted_list = []
    for char, count in chars.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
