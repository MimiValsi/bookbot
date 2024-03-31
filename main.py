def read_file(path):
    with open(path) as f:
        return f.read()

def number_of_words(string):
    words = string.split()
    return len(words)

def number_of_times(string):
    times = {}
    low_string = string.lower()
    for char in low_string:
        if not char in times:
            times[char] = 1
        else:
            times[char] += 1
    return times

def sort_on(d):
    return d["num"]

def dict_sorted(dic):
    sorted_list = []
    for char in dic:
        sorted_list.append({"char": char, "num": dic[char]})
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

def main():
    book = "books/frankenstein.txt"
    file = read_file(book)
    number = number_of_times(file)
    sorted_list = dict_sorted(number)
    print(f"--- Begin report of {book} ---")
    print(f"{number} words found in the document")
    print()

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The {item['char']} character was found {item['num']} times")

    print("--- End report ---")


main()
