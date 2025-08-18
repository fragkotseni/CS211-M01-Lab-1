"""
Project/File Name: ___________________________
Author:           ___________________________
Date Created:     ___________________________
Last Modified:    ___________________________

Purpose:          [Brief description of what this file/project does]

Dependencies:     [List any required libraries, modules, or files]
Usage:            [How to run or use this file/project]
Inputs:           [Describe expected input, if any]
Outputs:          [Describe output, if any]
Notes:            [Any additional important information]
"""

#
"""
START
Display a welcome message to the customer
Define a menu with food items and their prices (e.g., Burger - $5, Pizza - $8, Salad - $4, Soda - $2)
Initialize total order amount to 0
LOOP (repeat until the customer is done ordering):
    Display the menu with item numbers and prices
    Ask the customer to enter the item number they want to order
    Ask the customer to  geenter the quantity for that item
    Calculate the cost for this item:
    item cost = price of item * quantity
    Add the item cost to the total order amount
    Ask the customer if they want to order another item (yes/no)
    IF the answer is "no":
        Exit the loop
Display the total order amount to the customer
Display a thank you message
END
"""
name = input("Hello what's your name? \n")
print("Hello " + name + " ,welcome to our restaurant!")
print("Our menu: ")

menu = {
    1: ("Burger", 5),
    2: ("Pizza", 8),
    3: ("Salad", 4),
    4: ("Soda", 2)
}

total = 0  

while True:
    for number, (item, price) in menu.items():
        print(f"{number}. {item} - ${price}")

    choice = int(input("Enter the item number you want to order: "))
    if choice < 1 or choice > 4:
        print("Invalid choice. Try again.")
        continue

    quantity = int(input(f"How many would you like? "))

    cost = menu[choice][1] * quantity
    total += cost
    print(f"Added {quantity} x {menu[choice][0]} = ${cost}")

    more = input("Do you want to order another item? (yes/no): ").lower()
    if more != "yes/no":
        print ("Invalid Choice!")
        continue
    elif more != "yes":
        break

print(f"\nYour total order amount is: ${total}")
print("Thank you for your order!")