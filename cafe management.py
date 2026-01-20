menu = {'pizza' : 100, 'burger' : 50, 'coffee' : 60, 'sandwich' : 40, 'maggie' : 50, 'hotdog' : 50,}

print("Welcome to Dev's kitchen, here's our menu?\n" \
"\nPizza: 100 \nBurger: 50 \nCoffee: 60 \nSandwich: 40 \nMaggie: 50 \nHotdog: 50")

while True:
    item_1 = input("What woulld you like to order? ").lower()
    if item_1 in menu:
        print(f"{item_1} added to your order list")
        break
    else:
        print('Invalid input')

order_value = 0
order_value += menu[item_1]

while True:
    user_input = input("Would you like to order something more?(y/n): ").lower()
    if user_input == "y":
        item_2 = input("What else woulld you like to order? ").lower()
        if item_2 not in menu:
            print('Invalid input')
        print(f"{item_2} added to your order list")
        order_value += menu[item_2]
    elif user_input == 'n':
        print("Thanks for ordering.")
        break
    else:
        print("Invalid Input")

print('Your total order value is: ', order_value)