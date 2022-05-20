"""Author: Ryan Miskovic
Date: 5/20/2022
Program purpose: This program reverses a user input name."""

name = input("Enter your first name: ")
NEW_NAME = ""
print(name)
for ch in reversed(name):
    NEW_NAME += ch

print(NEW_NAME)
