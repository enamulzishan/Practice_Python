print("Welcome to my Password generator")
import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-+"
password = ""
for _ in range(8):
    password += random.choice(characters)
print("Your generated password is:", password)