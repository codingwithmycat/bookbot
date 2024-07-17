def main():
    report()

def count_characters(text):
    ch_freq = {}
    for string in text:
        lowered_string = string.lower()
        for ch in lowered_string:
            if ch not in ch_freq:
                ch_freq[ch] = 1
            else:
                ch_freq[ch] += 1
    return ch_freq

def convert_to_list_of_dict(dict):
    as_list_of_dict = []
    temp_dict = {}
    for k, v in dict.items():
        temp_dict["char"] = k
        temp_dict["num"] = v
        as_list_of_dict.append(temp_dict)
        temp_dict = {}
    return as_list_of_dict        

def sort_on(dict):
    return dict["num"]

def report():
    book = []
    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        book = file_contents.split()
        
    print(f"{len(book)} words found in the document")

    char_count = count_characters(book)
    as_list = convert_to_list_of_dict(char_count)
    as_list.sort(reverse=True, key=sort_on)

    for item in as_list:
        message = ""
        if item["char"].isalpha():
            message = "The " + "'" + item["char"] + "'" + " character was found " + str(item["num"]) + " times"
            print(message)
        
    print("--- End report ---")


main()

