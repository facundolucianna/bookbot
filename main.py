def count_words(txt: str) -> int:
    return len(txt.split())


def count_chars(txt: str) -> dict:
    output_dict = {}
    for i in "abcdefghijklmnoprstuvwxyz":
        counter = 0
        for char in txt.lower():
            if char == i:
                counter += 1

        output_dict[i] = counter

    return output_dict


with open("./books/frankenstein.txt", "r") as file:
    text = file.read()

fran_words = count_words(text)
char_dict = count_chars(text)
print("--- Begin report of books/frankenstein.txt ---")
print(f"{fran_words} words found in document")
max_value = -9000
keys = list(char_dict.keys())
while len(keys) != 0:
    for char in keys:
        if char_dict[char] > max_value:
            max_value = char_dict[char]
            last_key = char
    print(f"The '{last_key}' character was found {char_dict[last_key]} times")
    keys.remove(last_key)
    max_value = -9000
print("--- End report ---")
# print("hello world")
