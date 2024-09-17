def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = total_number_words(text)
    print(text.split())
    print(f"{words} total words")


def total_number_words(text):
    return len(text.split())


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
