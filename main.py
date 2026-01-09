import sys
from stats import get_chars_dict, get_num_words, sort_chars_dict

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    chars_dict = get_chars_dict(book_text)
    sorted_chars_dict = sort_chars_dict(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("----------- Character Count ----------")
    for item in sorted_chars_dict:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
