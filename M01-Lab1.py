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

# Ask the user for their name
name = input("Hello what's your name? \n")

# Greet the user with a welcome message
print("Hello " + name + " ,welcome to our restaurant!")

# Show a menu header
print("Our menu: ")

# Define a dictionary for the menu items
# Keys = item numbers, Values = (item name, price)
menu = {
    1: ("Burger", 5),
    2: ("Pizza", 8),
    3: ("Salad", 4),
    4: ("Soda", 2),
    5: ("Coffee", 3)
}

# Variable to keep track of the total cost
total = 0  

# Start an ordering loop
while True:

    # Display the menu items
    for number, (item, price) in menu.items():
        print(f"{number}. {item} - ${price}")

    # Ask the user to choose an item by number
    choice = int(input("Enter the item number you want to order: "))

     # Validate the choice 
    if choice < 1 or choice > 5:
        print("Invalid choice. Try again.")
        continue

    # Ask how many of that item the user wants
    quantity = int(input(f"How many would you like? "))

     # Calculate cost for this order
    cost = menu[choice][1] * quantity
    total += cost # Add cost to total

    # Confirm what was added
    print(f"Added {quantity} x {menu[choice][0]} = ${cost}")

    more = input("Do you want to order another item? (yes/no): ").lower()
    if more == "yes":
        # continue the ordering process
        continue
    elif more == "no":
        # stop ordering
        break
    else:
         # If input is not valid
        print("Invalid choice! Please enter 'yes' or 'no'.")

# Print the total bill after the loop ends
print(f"\nYour total order amount is: ${total}")

# Thank the customer
print("Thank you for your order!")