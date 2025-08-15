from stats import get_num_words, get_chars_dict, sort_on
import sys

'''
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"{num_words} words found in the document")
    print(chars_dict)
'''#this is for the previous solution

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    sorted_chars = sort_on(chars_dict)
    #print(sorted_chars)
    for char, count in sorted_chars.items():
        if char.isalpha():  # only show letters
            print(f"{char}: {count}")

    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()