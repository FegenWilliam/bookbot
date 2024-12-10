def sort_on(dict):
    for key in dict:
        return dict[key]

def list_of_dict_conrvert(dict):
    list_dict = []
    for key in dict:
        num = dict[key]
        char_dict = {key: num}
        list_dict.append(char_dict)
    list_dict.sort(reverse=True,key=sort_on)
    return list_dict
def report(bookpath,wordcount,list_dict):
    
    print(f"--- Begin report of {bookpath} ---")
    print(f"{wordcount} words found in the document")
    for dict in list_dict:
        for key in dict:
            char = key
            num = dict[key]
        print(f"The {char} character was found {num} times")
    print("--- End report ---")
def count_char(text):
    lowered_words = text.lower()
    count_dict = {}
    for char in lowered_words:
        if char.isalpha():
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
    list_dict = list_of_dict_conrvert(char_count)
    report(book_path,count_word,list_dict)
    
    
main()