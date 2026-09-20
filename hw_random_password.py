import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password += random.choice(characters)

password = list(password)
random.shuffle(password)
password = ''.join(password)

print("Random Password:", password)