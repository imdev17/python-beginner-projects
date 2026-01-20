import random

char = ("abcdefghijklmnopqrstuvwxyvABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#*_-.")
try:
    length = int(input('Enter passwrod length: '))
except ValueError:
    print("Invalid Input")
password = ""

for a in range(length):
    password += random.choice(char)
print("Your password is: ",password)