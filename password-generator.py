#import re
import random

input = input()
password = ''
size = None
#alphabet = 'abcdefghijklmnopqrstuvwxyz'
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%&*()'  #(0, 26) Only Letters | 27, 37 Only Numbers | (38, ...) Only Symbols
symbols = ''
#numbers = (0,1,2,3,4,5,6,7,8,9)

#options
enableNumbers = True
enableSymbols = True

def pickRandomLetter():
    if enableNumbers and enableSymbols == False:
        randomCharIndex = random.randrange(0, 26)
        return chars[randomCharIndex]
    elif enableNumbers == True and enableSymbols == False:
        randomCharIndex = random.randrange(0, 36)
        return chars[randomCharIndex]
    elif enableNumbers == False and enableSymbols == True:
        randomCharIndex = random.randrange(0, 26) + random.randrange(38, 46)
        return chars[randomCharIndex]
    elif enableNumbers and enableSymbols == True:
        randomCharIndex = random.randrange(0, 46)
        return chars[randomCharIndex]

def Generator():
    global password
    while len(password) < size:
        randomChar = pickRandomLetter()
        password += randomChar
        if len(password) == size:
            break

def Configurator():
    input = int(input("Choose the password size (8-72)\n"))
    global size
    #Set to 8 if less
    if input < 8:
        size = 8
        print("The min size is 8 chars\n ")
    #Set to 72 if greater
    elif input > 72:
        size = 72
        print("The max size is 72 characters.")
    else:
        size = input
    print(f"Password size: {size}\n")

def Start():
    Configurator()
    Generator()

### START ###
Start()

print(f"Your password is: {password}")