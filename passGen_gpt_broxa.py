import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'
password = ''
size = 10

def pickAlphabetLetter():
    randomCharIndex = random.randrange(0, 26)
    return alphabet[randomCharIndex]

def generator():
    global password
    while len(password) < size:
        randomChar = pickAlphabetLetter()
        password += randomChar
        if len(password) == size:
            break

generator()
print(f"Generated password: {password}")
