import sys
from stats import get_word_count, get_character_count, sorted_list_of_dicts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print('----------- Word Count ----------')
    print(f"Found {get_word_count(book_text)} total words")
    char_count = get_character_count(book_text)
    print('--------- Character Count -------')
    sorted_char_count = sorted_list_of_dicts(char_count)
    for item in sorted_char_count:
        print(f"{item['character']}: {item['count']}")
    print('============= END ===============')
main()