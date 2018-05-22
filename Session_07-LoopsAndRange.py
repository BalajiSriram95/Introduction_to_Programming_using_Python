#for Loop: For Each item in Our List, Do This

prices = [2.50, 3.50, 4.50]

# price is a temporary variable that holds one
# of the prices in the list for each run.
for price in prices:
    print('Price is', price)
# Like saying “do this”
# for each number price in our list prices
# The loop runs one time for each price in the list.

#Using a for Loop to Sum Our Prices
# Average price
total = 0
prices = [2.50, 3.50, 4.50]
# Average price
for price in prices:
    print('Price is', price)
    # We can add to our total and print total to see it changing.
    total = total + price
    print('total is', total)

for price in prices:
    total = total + price

# After the loop, we compute the average.
average = total/len(prices)
print('avg is', average)

# Generating a Random coupon Number

# how do we get a single random number?
import random
# Gives us a random number from [0.0, 1.0)
r1 = random.random()
print(r1)

# Gives us a random choice from a list
r2 = random.choice([1,2,3,4,5])
print(r2)

# Gives us a random number in this range
r3 = random.randint(1, 1000) + random.random()
print(r3)

import random
# What do we put here if we don’t have a list?
#for i in ???:
#    print(ticket)
#    ticket = random

# How do we iterate through the for loop 10 times?
range(10)

#range(count) generates a list of [0, …, count-1] behind the scenes.
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

import random
for i in range(10):
    rand_coupon = random.randint(1, 1000)
    print(rand_coupon)

# Getting More Specific With range()
#            start stop step
for i in range(100, 110, 3):
    print(i)


# Create Our own list from given list
fruits = ['Banana', 'Cherry', 'Grape', 'Watermelon']

basket = []
for fruit in fruits:
    # For each fruits fruit in our list, we’ll concatenate kg's to it,
    # and we’ll add that to our menu list.
    basket.append(fruit + ' - 1kg')

print(basket)


# Create Our own dist from given dist
fruits = ['Banana', 'Cherry', 'Grape', 'Watermelon']
#           10          20      30          40

# Let's store the basket items with their prices in a dictionary
basket_prices = {}
price = 10
iterable = 1
for fruit in basket:
    price = price * iterable
    # The fruit is the key — for example, 'Banana - 1kg' is the key and Rs10 is the value.
    basket_prices[fruit] = price
    #iterable = iterable + 1
    iterable += 1

print(basket_prices)

# Could we print out each item in our dictionary in a loop like a list?
for fruit_price in basket_prices:
    # This will default to just printing the keys in a dictionary.
    print(fruit_price)
fruitsandprices = {'Banana - 1kg' : 20, 'Cherry - 300gs' : 30, 'Grape - 1kg' : 40, 'Watermelon - 2kg' : 50}
for name, price in fruitsandprices.items():
    # Now the loop has access to both the key and the value here — name and price.
    print(name, ': Rs', price)

# Note: To get a list of the keys in a dictionary, use fruit_price.keys()
#       and to get a list of the values in a dictionary, use fruit_price.values()

#Let’s get rid of the unnecessary spaces in our output.
for name, price in fruitsandprices.items():
    print(name, ': Rs',price, sep='')
# print() defaults to having a space to separate each word. We can override this by
# setting sep = empty string.

# Banana - 1kg : Rs 10
# Cherry - 1kg : Rs 20
# Grape - 1kg : Rs 30
# Watermelon - 1kg : Rs 40

# Rounding a Float to a Certain Number of Decimal Places
for name, price in basket_prices.items():
    # We can format our price float to two decimal
    # places using the built-in 2 decimal places, format() function.
    print(name, ': Rs',format(price, '.2f'), sep='')



# A Simple while Loop Example
# A while loop would be better since while loops continue looping while a condition is True
x = 1
while x != 3:
    print('x is', x)
    x = x + 1

# Lets Add Fruits to Basket in Shop
fruits_shop = {'Banana - 1kg': 10, 'Cherry - 1kg': 20, 'Grape - 1kg': 60, 'Watermelon - 1kg': 240}
shopping_items = []
shopping_item = input("What would you like to shop in our shop? (Q to Quit)")

# If we don’t change “order” in the loop, it will never be “Q” and the loop will never stop running.
while (shopping_item.upper() != 'Q'):
    # Find the shopping item and add it to the list if it exists
    # Try to get() the item from fruits_shop
    found = fruits_shop.get(shopping_item)
    # If it exists, add it to the list
    if found:
        shopping_items.append(shopping_item)
    else:
        # If not, let the customer know
        print("selected item doesn't exist")

    # See if the customer wants to shop anything else
    shopping_item = input("Anything else? (Q to Quit)")

print(shopping_items)


# Another Way to Break Out of the Loop
fruits_shop = ['Banana', 'Cherry', 'Grape', 'Watermelon']
shopping_items = []
shopping_item = input("What would you like to shop in our shop? (-1 to Quit)")

# If we don’t change “order” in the loop, it will never be “Q” and the loop will never stop running.
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
    found = fruits_shop[shopping_item]
    # If it exists, add it to the list
    if found:
        shopping_items.append(fruits_shop[shopping_item])
    else:
        # If not, let the customer know
        print("selected item doesn't exist")

print(shopping_items)


# Using Continue for Special Cases in the Loop
fruits_shop = {'Banana - 1kg': 10, 'Cherry - 1kg': 20, 'Grape - 1kg': 60, 'Watermelon - 1kg': 240}
shopping_items = []
shopping_item = input("What would you like to shop in our shop? (Q to Quit)")

# If we don’t change “order” in the loop, it will never be “Q” and the loop will never stop running.
# Always run the loop forever..
while (True):
    if shopping_item == 'Dragon Fruit':
        print('Sorry, we''re out of that stock!')
        continue
    # unless the user types “Q,” then break out of the loop.
    if shopping_item.upper() == 'Q':
        break
    # Find the shopping item and add it to the list if it exists
    # Try to get() the item from fruits_shop
    found = fruits_shop.get(shopping_item)
    # If it exists, add it to the list
    if found:
        shopping_items.append(shopping_item)
    else:
        # If not, let the customer know
        print("selected item doesn't exist")

    # See if the customer wants to shop anything else
    shopping_item = input("Anything else? (Q to Quit)")

print(shopping_items)


# Fixing of our Infinite Loop problem
fruits_shop = {'Banana - 1kg': 10, 'Cherry - 1kg': 20, 'Grape - 1kg': 60, 'Watermelon - 1kg': 240}
shopping_items = []
shopping_item = input("What would you like to shop in our shop? (Q to Quit)")

# If we don’t change “order” in the loop, it will never be “Q” and the loop will never stop running.
# Always run the loop forever..
while (True):
    # See if the customer wants to shop anything else
    shopping_item = input("Anything else? (Q to Quit)")

    if shopping_item == 'Dragon Fruit':
        print('Sorry, we''re out of that stock!')
        continue
    # unless the user types “Q,” then break out of the loop.
    if shopping_item.upper() == 'Q':
        break
    # Find the shopping item and add it to the list if it exists
    # Try to get() the item from fruits_shop
    found = fruits_shop.get(shopping_item)
    # If it exists, add it to the list
    if found:
        shopping_items.append(shopping_item)
    else:
        # If not, let the customer know
        print("selected item doesn't exist")

print(shopping_items)
