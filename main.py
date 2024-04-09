def main():
    path = "books/frankenstein.txt"
    file_contents = get_book_text(path)
    word_count = count_words(file_contents)
    letter_count = count_letters(file_contents)
    sorted_list = sort_letter_count(letter_count)

    # Format and print results to the terminal
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} was found in the document\n")

    for ele in sorted_list:
        char = ele["char"]
        count = ele["count"]

        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

    print("--- End report ---")
    
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_count = {}
    for ch in text:
        char = ch.lower()
        if char not in letter_count:
            letter_count[char] = 0
        letter_count[char] += 1
    return letter_count

def sort_letter_count(letter_count):
    sorted_list = []
    for ch in letter_count:
        sorted_list.append({"char": ch, "count": letter_count[ch]})
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["count"]

main()