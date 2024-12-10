def count_char():
    words = get_book_text()
    lowered_words = words.lower()
    count_dict = {}
    for char in lowered_words:
        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1
    return count_dict

def count_words():
    words = get_book_text()
    words_no_ws = words.split()
    count = len(words_no_ws)
    return count
def get_book_text():
    with open("books/frankenstien.txt") as f:
        file_contents = f.read()
    return file_contents

def main():
    print(count_char())
    count = count_words()
    print(count)
main()