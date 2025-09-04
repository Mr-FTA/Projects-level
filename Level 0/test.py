import string
import time
import sys

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)

text = input("Enter text: ")

output = ""

for char in text:
    if char in lowercase:
        letters = lowercase
    elif char in uppercase:
        letters = uppercase
    else:
        output += char
        print('\r' + output, end='', flush=True)
        continue

    index = letters.index(char)


    for i in range(index + 1):

        print('\r' + output + letters[i], end='', flush=True)
        time.sleep(0.05)


    output += letters[index]

print()
input()
