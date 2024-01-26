def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    char_counts = {}
    for c in alphabet:
        char_counts[c] = get_num_char(text, c)
    print(f"--- Begin report of {book_path} ---")
    print(f"{get_num_words(text)} words found in the document\n")

    for c in char_counts:
        print(f"The '{c}' character was found {char_counts[c]} times")
    print("--- End report ---")
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text, char):
    text = text.lower()
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()