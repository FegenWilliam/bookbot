def count_char(text):
    lowered_words = text.lower()
    count_dict = {}
    for char in lowered_words:
        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1
    return count_dict

def count_words(text):
    words_no_ws = text.split()
    count = len(words_no_ws)
    return count
def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstien.txt"
    text = get_book_text(book_path)
    count_word = count_words(text)
    char_count = count_char(text)
    print(count_word)
    print(char_count)
    
    
main()