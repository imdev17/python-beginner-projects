import random

# This program simulates rolling two dice and displays the result.
# The user is prompted to roll the dice by entering 'y' or 'n'.

while True:
    opt = input("Do you want to roll the die? (y/n): ").lower()

    if opt == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(die1, die2)
    elif opt =="n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")