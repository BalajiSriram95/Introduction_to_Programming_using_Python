#Comparing Lists
#How do we check if two lists are equal?

my_list = [1, 2, 3, 4]
your_list = [4, 3, 2, 1]
his_list = [1, 2, 3, 4]

print(my_list == your_list) # -> False
print(my_list == his_list) # -> True

# Two lists need to have the same values
# in the same order to be equal.


#Comparing Dictionaries
#How do we check if two dictionaries are equal?

my_dict = {1:1, 2:2, 3:3, 4:4}
your_dict = {4:3, 3:3, 2:2, 1:1, 5:5}

print(my_dict == your_dict)
# -> True

# Since dictionaries aren’t ordered, they only
# need to have the same key-value pairs
# to be equal.


#Let’s say we have three separate lists:
#How would we combine these into one list?
even_num = [2, 4, 6, 8]
odd_num = [1, 3, 5, 7]
whole_num = [-2, -1, 0, 1, 2]

#A List of Lists
#You can have a container of containers —
# Numbers is a list of type of number, and each type of number is a list of numbers.

numbers = [[2, 4, 6, 8],
            [1, 3, 5, 7],
            [-2, -1, 0, 1, 2]]

# list of list [[], [], []]

#Getting an Item From a Two-dimensional List
# The list at index 0 in the outer list
print('Even Numbers:\t', numbers[0])
print('Odd Number:\t', numbers[1])
print('Whole Number:\t', numbers[2])

# Even Numbers: [2, 4, 6, 8]
# Odd Number: [1, 3, 5, 7]
# Whole Number: [-2, -1, 0, 1, 2]

emp1 = {"fn" : "Balaji", "ln" : "Sriram"}
emp2 = {"fn" : "Python", "ln" : "Training"}
emp3 = {"fn" : "Employee", "ln" : "Employeer"}

# The list at index 0 in the outer list,
# the item at index 1 in the inner list
#fruitsandcolours['Grape']
print(numbers[0][1])
# -> 4
# It would be better if we didn’t have to know
# even numbers was at index 0, odd numbers at 1, etc.



#A Dictionary of Lists
#We can use a dictionary with keys for Even Numbers, Odd Number, and Whole Number.
numbers = {  'even_num' : [2, 4, 6, 8],
              'odd_num' : [1, 3, 5, 7],
            'whole_num' : [-2, -1, 0, 1, 2]
          }

print('Even Numbers:\t', numbers['even_num'])
print('Odd Number:\t', numbers['odd_num'])
print('Whole Number:\t', numbers['whole_num'])

# ->    Even Numbers: [2, 4, 6, 8]
# ->    Odd Number: [1, 3, 5, 7]
# ->    Whole Number: [-2, -1, 0, 1, 2]


##Even Test Similar like above try with List of Dictionaries
# with give below 3 dictionaries variables
# emp1 = {"fn" : "Balaji", "ln" : "Sriram"}
# emp2 = {"fn" : "Python", "ln" : "Training"}
# emp3 = {"fn" : "Employee", "ln" : "Employeer"}