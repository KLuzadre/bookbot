def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
    print(len(words))

count()