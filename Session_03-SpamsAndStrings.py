#Creating Strings
#Single or double quotes work — just be consistent
my_str = 'Hello World'
print(my_str)

my_str1 = "SPAM95"
print(my_str1)

#String Concatenation With +
first_name = 'Cherry'
last_name = 'Python'
full_name = first_name + last_name #Need to add a space
print(full_name)

#Concatenating a Space
first_name = 'Cherry'
last_name = 'Python'
full_name = first_name + ' ' + last_name #Need to add a space
print(full_name)
print(first_name,last_name)

#Concatenating Strings and Ints
name = 'Cherry Python'
description = 'sketch comedy group'
year = str(1969)
#sentence = name + ' is a ' + description + ' formed in ' + year #Year is an int, not a string
#TypeError: Can't convert 'int' object to str implicitly

#Let's Try to fix this
year = '1969' #ü We could add quotes and make the year a string instead of an int

sentence = name + ' is a ' + description + ' formed in ' + year
print(sentence)
#This will work, but it really makes sense to keep numbers as numbers.
#print() Casts to String Automatically
print(name, 'is a' , description, 'formed in' , year)


#Dealing With Quotes in Strings
#**famous_sketch = 'Hell's Grannies' '#Interpreter thinks the quote has ended and doesn’t know what S is
#Syntax Error: invalid syntax
#Start with '' instead — now the ' no longer means the end of the string
famous_sketch1 = 'Hell\'s Grannies'
print(famous_sketch1)


#Special Characters — Newline
famous_sketch1 = "\nHell's Grannies" #Add a newline to make this look better
famous_sketch2 = '\nThe Dead Parrot'
print('Famous Work:', famous_sketch1, famous_sketch2)
'''Famous Work:
Hell's Grannies
The Dead Parrot'''

#This works, but we want to indent the titles

#\t is a special character that means tab
famous_sketch1 = "\n\tHell's Grannies" #Add a tab to indent and make this look even better
famous_sketch2 = '\n\tThe Dead Parrot'
print('Famous Work:',famous_sketch1, famous_sketch2)

# here \n means newline!
print('C:\some\name')

# note the r before the quote
print(r'C:\some\name')

#One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string,
# but it’s possible to prevent this by adding a \ at the end of the line. The following example:
print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
#produces the following output (note that the initial newline is not included):

#Strings can be concatenated (glued together) with the + operator, and repeated with *:
## 3 times 'un', followed by 'ium'
print(3 * 'un' + 'ium')
#SyntaxError: invalid syntax => add + sign
print('un' * 3+ 'ium')

#feature is particularly useful when you want to break long strings
text = ('Put several strings within parentheses '
        'to have them joined together.'
       )
print(text)

text = 'Python ' \
       'Programme'
print(text)

text = 'Python ' 'Programme'
print(text)


#Strings Behind the Scenes — a List of Characters
#greeting = 'H E L L O W O R L D !'
#          [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10][11]
#Starts at 0
greeting = 'HELLO WORLD!'
print(greeting[0]) #We can get each character by calling its index with []
print(greeting[11])
#print(greeting[12])  #IndexError: string index out of range

#String Built-in Function — len()
#There are a few built-in string functions — like len(), which returns the length of a string and is very useful
greeting = 'HELLO WORLD!'
print(len(greeting))

print(greeting[-2] + greeting[-4])


#The Man Who Only Types Shortcut of Words
word1 = 'Good'
word2 = 'Evening'
sc1 = word1[0] + word2[0] #The first letter of the word: characters at positions [0] and [0]
print(sc1)


#Using Slices to Access Parts of a String
word = "Python"
print(word[5])
#Start boundary : End boundary

#Slice Formula and Shortcuts
#slice formula: variable [start : end+1]
print(word[0:2] + word[2:7])

#Shortcuts
word[:2]
word[2:]

print(word[-4:])
print(word[0])

#Using the String Slice Shortcut
word1 = 'Good'
end1 = word1[2:]

word2 = 'Evening'
end2 = word2[3:]

print(end1, end2)


#The Index at the Halfway Point
#The len() function will let us calculate the halfway index of our word
word1 = 'Good'
half1 = len(word1) / 2
print(half1)
#half1 is 2.0
word2 = 'Evening'
half2 = len(word2) / 2
print(half2)
#print(word2[half2])
#half2 is 3.5
#PROBLEM: indexes have to be integers — floats won’t work!

#// 2 division signs means integer division in Python
word1 = 'Good'
half1 = len(word1) // 2 #// Means integer division
print(half1)
#half1 is 4//2 = 2

word2 = 'Evening'
half2 = len(word2) // 2
print(half2)
print(word2[half2])
#// Also rounds down to the nearest integer
#half2 is 7//2 = 3

word2 = 'Evening'
print(word2[::-3])


#Making Our Program More Reusable
word1 = 'Good'
half1 = len(word1) // 2
end1 = word1[2:]
#// Means integer division
word1[half1:]

word2 = 'Evening'
half2 = len(word2) // 2
end2 = word2[3:]
#OR
word2[half2:]
print(end1, end2)

#String Membership Test
print('a' in 'program')

print('at' not in 'battle')


##Event Test
#He said, "Welcome to Introduction to Python Programming"
#1st Need to print in this format of text 'He said, "Welcome to Introduction to Python Programming"'
#2nd
#   1st Red, Orange, Yellow, Green, Purple, Indigo, Maroon, White
#   2nd concatenate above each colour with Fruit or Vegetable name
#3rd Need to print given string in a reverse order
#4th Need to print Raw String to ignore escape sequence
#   Example Output: This is a
#                   good example
#src string: This is \x61 good example

#Common Python String Methods
#There are numerous methods available with the string object.
# The format() method that we mentioned above is one of them.
# Some of the commonly used methods are lower(), upper(), join(), split(), find(), replace() etc.
print("PrOgRaMiZ".lower())

print("PrOgRaMiZ".upper())

print("This will split all words into a list".split())

print(' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string']))

#Return the lowest index in the string where substring sub is found within the slice s[start:end].
#   Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.
print('Happy New Year'.find('e'))
#The find() method should be used only if you need to know the position of sub.
# To check if sub is a substring or not, use the in operator:
print('e' in 'Python')

'Happy New Year'.replace('Happy','Brilliant')