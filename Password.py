#Name Sudhir Gaikwad
#CodSoft Internship 
# Task 3

import random
import string

length = int(input("Enter Length"))

def generate_password(length, include_uppercase=True, include_digits=True, include_symbols=True):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password = generate_password(length)
print("Generated Password:", password)