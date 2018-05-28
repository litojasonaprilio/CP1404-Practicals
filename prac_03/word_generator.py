import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = str(input("Enter the word format using c as random consonants and v as random vowels: "))


def is_valid_format():
    if word_format == "c" or word_format == "v":
        return True
    else:
        print("Please insert the correct letter!")
        return False


check = is_valid_format()
word = ""
for kind in word_format.lower():
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)


print(word)