import sys
import re

PROPN = open('lists/nombres-propios-es.txt', 'r')
LAST_NAMES = open('lists/apellidos-es.txt', 'r')
word_list = []
dictionary = set()


def read_dictionary_file():
    global dictionary
    if dictionary:
        return

    with open ("lists/es.txt", "r") as f:
        contents = f.read()

    dictionary = set(
        word.lower()
        for word in contents.splitlines()
    )

def is_spelled_correctly(word):
    # Return true if spelled correctly, false otherwise
    read_dictionary_file()
    return word in dictionary


with open('outputmorpho.txt', 'r') as f:
    for line in f:
        if line[0] == "\"":
            if not re.findall('[\.\,\¡\!\¿\?]', line):
                word_list.append(line[2:-3])

f.close()

# If the word is not a proper noun or a last name -> lowercase
for word in word_list:
    if word not in PROPN.read() and LAST_NAMES.read():
        word_list = [word.lower() for word in word_list]

# If the word is not spelled correctly, print it
for word in word_list:
    if not is_spelled_correctly(word):
        print("\tThis is a spelling error: <" + word + ">")
