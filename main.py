def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
    print(len(words))

def char_count():
    char_dict = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_contents_lower = file_contents.lower()
        for char in file_contents_lower:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        for key in char_dict:
            if key.isalpha() == True:
                print(f"The '{key}' character was found {char_dict[key]} times")
    return char_dict

char_count()