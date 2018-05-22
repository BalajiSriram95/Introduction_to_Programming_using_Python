#A List Is a Container of Things
#Lists in Python are containers that can store anything you want.

# an empty list
empty = []

# list of numbers
nums = [10, 20, 30, 40.5]

# list of strings
words = ['Banana', 'Cherry', 'Grape', 'Watermelon']

# list of mixed items
anything = [10, 'Banana', True, 123.45]
asd123 = 123

a = [123.]

#A Python list is called an array in other languages, like JavaScript.

#An Item’s Index Is Its Position
#List items are ordered starting with index (or position) 0.
fruits = ['Banana', 'Cherry', 'Grape', 'Watermelon']
#   Index -> [0]     [1]         [2]         [3]


type(nums)
print(fruits[0]) # -> 'Banana'
fruits[3] # -> 'Watermelon'
# You can also slice a list to get a sub-section of the list.
print(fruits[1:3]) # -> ['Cherry', 'Grape']


fruits = ['Banana', 'banana', 'Grape', 'Watermelon']
# Index -> [-4]     [-3]         [-2]         [-1]

#Omitting the stop index slices to the end
#fruits[start:]
print(fruits[1:])

#Omitting the start index slices from the beginning
#fruits[:stop]
fruits[:3]


#Half-open ranges give complementary slices
fruits[1:] + fruits[:1] == fruits

#Omitting the start and stop indexes slices
# from the beginning to the end – a full slice
fruits[:]

# Copying lists
# Full slice: t = fruits[:]
# copy() method: u = fruits.copy()
# list() constructor: v = list(fruits)

a = [ [1,2], [3,4] ]
b = a[:]

a = [ax123, ax234] = ax3456
b = ax124890
b = [ax123, ax234]
#ax123 = a[0] = ax456
#ax234 = a[1]
#ax345 = a[]
#b = a[:]
b = a
b[0] = a[0]
#b = bx123 = a[]
#b[0] = ax123

print(a is b)


print(a == b)

print(a[0])

print(b[0])

print(a[0] is b[0])


a[0] = [10,12]
print(a[0])

print((b[0]))

a[1].append(5)

print(a[1])

print(b[1])


print(a)

print(b)
b[0] = a[0]

a.insert(0, [6,7,8])
a[0].remove(8)
del b[1]

a[0].append(21)


#Repetition
['Hello!', 12] * 4

# index(item) returns the integer index of the first equivalent element raises
# ValueError if not found
# count(item) returns the number of matching elements
print(fruits.count('banana'))
print(len(fruits))
#filter('anana'.match, fruits)

# The in and not in operators test for membership

a = 1
b = 20
listofnums = [1, 2, 3, 4, 5 ]

if a in listofnums:
   print ('Line 1 - a is available in the given list', listofnums.index(1) )
else:
   print ('Line 1 - a is not available in the given list')

if b not in listofnums:
   print ('Line 2 - b is not available in the given list')
else:
    print ('Line 2 - b is available in the given list')


#Creating a List and Adding Items
#Let’s create a list of Fruit names.
fruits = ['Banana', 'Cherry', 'Grape',]
print(fruits)

#Can create the list with elements in it already, or empty
fruits = []

# We can add items as we need.
fruits.append('Watermelon')
fruits.append('Guava')
fruits.insert(1,'Apple')
fruits[1] = 'Mango'

print(fruits)

# append() adds new items to the end of our list.
#fruits.append(item)
#['Banana', 'Cherry', 'Grape', 'Watermelon', 'Guava']



# Removing Elements
# We can remove items from our list by using the value or the index.
fruits = ['Banana', 'Cherry', 'Grape', 'Watermelon', 'Guava']
#      Index -> [0]     [1]         [2]         [3]     [4]

fruits.remove('Watermelon')
# Either OR
# depending on whether
# you know the value or the index
del fruits[3]

print(fruits)
# ['Banana', 'Cherry', 'Grape', 'Guava']

# We can also delete a slice.
fruits = ['Banana', 'Cherry', 'Grape', 'Guava']
del fruits[:2]
print(fruits)
# ['Grape', 'Guava']

