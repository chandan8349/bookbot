from stats import word_count, count_characters
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]


def get_book_text():
    with open(file_path, "r") as file:
        return file.read()


def sort_on(item):
    return item["num"]


def main():
    book_text = get_book_text()
    num_words = word_count(book_text=book_text)
    print("============ BOOKBOT ============")
    num_char = count_characters(book_text=book_text)
    print(f"Analyzing book found at books/{file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_char.sort(reverse=True, key=sort_on)
    for value in num_char:
        print(f"{value['char']}: {value['num']}")


if __name__ == "__main__":
    main()
