#Maintaining Two Lists
#What if we also wanted a list to keep track of the colour of fruit and fruit name in fruits list?
#If we do anything to one of our lists, we have to duplicate the operation in the other list.
fruits = ['Banana', 'Cherry', 'Grape', 'Watermelon', 'Guava']
colours = ['Yellow', 'Red', 'Black', 'DarkGreen', 'Green']
#   Index -> [0]      [1]     [2]        [3]        [4]

print(fruits[0], colours[0])

del fruits[0] #If we add or delete from one list…
del colours[0] #we have to do the same thing in the other list.

print(fruits)
print(colours)

#   ['Cherry', 'Grape', 'Watermelon', 'Guava']
#   ['Red', 'Black', 'DarkGreen', 'Green']

# We can improve upon this with dictionaries…

#A Dictionary Maps Keys to Values
#A dictionary is similar to a list, but you look up values by using a key instead of an index.
#   key    value
#'Banana'  'Yellow'
#'Grape'   'Black'

fruitsandcolours = {'Banana' : 'Yellow', 'Cherry' : 'Red', 'Grape' : 'Black', 'Watermelon' : 'DarkGreen', 'Guava' : 'Green'}
#                    key assign to value
# Each item is known as a “key-value pair”

print(fruitsandcolours['Banana'])
# To look up a value in a dictionary, we send in a key
# ( instead of index in a list ).

# 'Yellow'

#Dictionaries Can Hold Anything
# Dictionaries, like lists, can hold anything you want:
# numbers, strings, a mix of both, and other objects.

#Dictionary of strings to strings
fruitsandcolours = {'Banana' : 'Yellow', 'Cherry' : 'Red'}

#Dictionary of strings to numbers
fruitsandrupees = {'Banana' : 50, 'Cherry' : 80}

#Dictionary of anything
anything = {50:'watermelon', 'xyz':114.45}

#Creating a Dictionary and Adding Values
#Create an empty dictionary:
fruitsandcolours = {}

#Adding dictionary items:
fruitsandcolours['Banana'] = 'Yellow'
#print(fruitsandcolours)
#fruitsandcolours['Banana'] = 'Red'

fruitsandcolours['Cherry'] = 'Red'
fruitsandcolours['Grape'] = 'Black'

print(fruitsandcolours)

# => {'Banana' : 'Yellow', 'Cherry' : 'Red', 'Grape' : 'Black'}

#Updating Values in Our Dictionary
#Our current dictionary:
print(fruitsandcolours)

#Let’s update the value for smashing...
fruitsandcolours['Grape'] = 'light green'

#…and look up and print the same value.
print(fruitsandcolours['Grape'])

# -> 'light green'

#Removing Dictionary Items
#You can delete an item from a dictionary by looking up its key.

fruitsandcolours = {'Banana' : 'Yellow', 'Cherry' : 'Red', 'Grape' : 'light green'}

del fruitsandcolours['Grape'] #del will delete the key-value pair from the dictionary

print(fruitsandcolours)


# -> {'Banana' : 'Yellow', 'Cherry' : 'Red'}

#Get an Item That Might Not Be There
#Trying to access a key that doesn’t exist will cause an error.
#**print(fruitsandcolours['Grape'])
# -> KeyError: 'Grape'

#If you want to check if a word is in the dictionary, use get().
# Get a value that might not be there
output = fruitsandcolours.get('Grape')
print(output)
#Using get() is a best practice because it won’t crash your program.

#If the word WAS NOT in the dictionary -> None
#None is a type that represents the absence of a value.


#None Type
#None represents the absence of a value,
# and also evaluates to False in a conditional.

fruitsandcolours = {'Banana' : 'Yellow', 'Cherry' : 'Red'}

#Result equals None because the key doesn’t exist
output = fruitsandcolours.get('Grape')

if output:
    print(output)
else:
    print('Key does not exist')


