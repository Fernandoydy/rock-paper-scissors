import random

password = ''
size = None
alphabet = 'abcdefghijklmnopqrstuvwxyz'
#numbers = (0,1,2,3,4,5,6,7,8,9)

def pickRandomLetter():
    randomCharIndex = random.randrange(0, 26)
    return alphabet[randomCharIndex]

def generator():
    global password
    while len(password) < size:
        randomChar = pickRandomLetter()
        password += randomChar
        if len(password) == size:
            break

# START
input = int(input("Choose the password size (8-72)\n"))

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

print(f"The password size is: {size}\n")

generator()
print(f"Your password is: {password}")