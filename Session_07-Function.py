
# Problem: We’re Repeating a Lot of Code

fruits_shop = ['Banana', 'Cherry', 'Grape', 'Watermelon']
shopping_items = []
shopping_item = input("What would you like to shop in our shop? (-1 to Quit)")

# If we don’t change “order” in the loop, it will never be “-1” and the loop will never stop running.
# Always run the loop forever..
while (True):
    # See if the customer wants to shop anything else
    shopping_item = int(input("Anything else? (-1 to Quit)"))

    if shopping_item == 5:
        print('Sorry, we''re out of that stock!')
        continue
    # unless the user types “-1” then break out of the loop.
    if shopping_item == -1:
        break
    # Find the shopping item and add it to the list if it exists
    # Try to get() the item from fruits_shop
    found = fruits_shop[shopping_item]
    # If it exists, add it to the list
    if found:
        shopping_items.append(fruits_shop[shopping_item])
    else:
        # If not, let the customer know
        print("selected item doesn't exist")

print(shopping_items)


vegetable_shop = ['Tomato', 'Carrot', 'Beetroot', 'Potato']
shopping_items = []
shopping_item = int(input("What would you like to shop in our shop? (-1 to Quit)"))

# If we don’t change “order” in the loop, it will never be “-1” and the loop will never stop running.
# Always run the loop forever..
while (True):
    shopping_item = int(input("Anything else? (-1 to Quit)"))

    if shopping_item == 5:
        print('Sorry, we''re out of that stock!')
        continue
    # unless the user types “-1” then break out of the loop.
    if shopping_item == -1:
        break
    # Find the shopping item and add it to the list if it exists
    # Try to get() the item from fruits_shop
    found = vegetable_shop[shopping_item]
    # If it exists, add it to the list
    if found:
        shopping_items.append(vegetable_shop[shopping_item])
    else:
        # If not, let the customer know
        print("selected item doesn't exist")

print(shopping_items)

# Wouldn’t it be great to just have one piece of code for kind of fruits and Vegetables

# Functions Perform Specific Tasks

# Naming the Function
#def shopping():
    # Name: The name of the function is how we’ll run it later.
    # Colon : A colon marks the beginning of the function’s code.
    # Every function starts with def.

# Need to declare Function Parameters
# def shopping(shopping_item):

# Return Data From the Function
# def shopping(shopping_item):
#   ...
#   return shopping_items

# Return value:
# Functions may or may not return values this function returns the value of a variable called avg.
# Returning data from a function is optional.

# Putting Code in the shopping() Function
def shopping(item_no):
    while (True):
        # See if the customer wants to shop anything else
        if item_no == -9:
            item_no = int(input("Anything else? (-1 to Quit)"))

        if item_no == 5:
            print('Sorry, we''re out of that stock!')
            item_no = -9
            continue
        # unless the user types -1 then break out of the loop.
        if item_no == -1:
            break
        # Find the shopping item and add it to the list if it exists
        # Try to get() the item from fruits_shop
        found = fruits_shop[item_no]
        # If it exists, add it to the list
        if found:
            shopping_items.append(fruits_shop[item_no])
            item_no = -9
        else:
            item_no = -9
            # If not, let the customer know
            print("selected item doesn't exist")

    return shopping_items

fruits_shop = ['Banana', 'Cherry', 'Grape', 'Watermelon']
print(fruits_shop)
shopping_items = []
shopping_item_no = int(input("What would you like to shop in our shop? (-1 to Quit)"))

shopping_items = shopping(shopping_item_no)
print(shopping_items)


##Even Test With using function like above instead of list use dictionary
#fruitsandprices = {'Banana - 1kg' : 20, 'Cherry - 300gs' : 30, 'Grape - 1kg' : 40, 'Watermelon - 2kg' : 50}

# main() and Calling main()
# A best practice is to organize our main program code into a function called main()
def shopping(item_no):
    while (True):
        # See if the customer wants to shop anything else
        if item_no == -9:
            item_no = int(input("Anything else? (-1 to Quit)"))

        if item_no == 5:
            print('Sorry, we''re out of that stock!')
            item_no = -9
            continue
        # unless the user types -1 then break out of the loop.
        if item_no == -1:
            break
        # Find the shopping item and add it to the list if it exists
        # Try to get() the item from fruits_shop
        found = fruits_shop[item_no]
        # If it exists, add it to the list
        if found:
            shopping_items.append(fruits_shop[item_no])
            item_no = -9
        else:
            item_no = -9
            # If not, let the customer know
            print("selected item doesn't exist")

    return shopping_items

def main():
    fruits_shop = ['Banana', 'Cherry', 'Grape', 'Watermelon']
    print(fruits_shop)
    shopping_items = []
    shopping_item_no = int(input("What would you like to shop in our shop? (-1 to Quit)"))

    shopping_items = shopping(shopping_item_no)
    print(shopping_items)

main()

# Order of Execution
# 1. All of the execution starts from main()
# 2. Then runs all of the code under main()
# 3. The shopping() function will only run when it gets called.

# Understanding Local Scope
# Understanding Global Scope

def check_number(number):
    if number >= 0:
        print("Positive or Zero")
        # prime numbers are greater than 1
        if number > 1:
            # check for factors
            if (number % 2) == 0:
                print(number, "is a even number")
            else:
                print(number, "is not a odd number")
    else:
        print("Negative number")

num = 10
check_number(num)

