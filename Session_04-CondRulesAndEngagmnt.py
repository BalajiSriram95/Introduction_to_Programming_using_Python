# Comparison Operators
# < --less than

# <= --less than equal to

# == --equal to

# >= --greater than equal to

# > greater than

# != not equal to

print(5 < 10)
# Is 5 less than 10 ?? True

name = 'Pam' #Setting the name variable equal to 'Pam'
print(name == 'Jim')
# Is name equal to Jim ?? False

print(5 == 10)
# Is 5 equal to 10 ?? False

print(name != 'Jim')
# Is name NOT equal to Jim ?? True

print(5 > 10) # False

print(5 <= 10) # True

print(5 >= 10) # False


#Booleans
#In programming, a boolean is a type that can only be True or False.
#True => T
#False => F
is_raining = True
print(is_raining)


#Conditional — if, then
#An if statement lets us decide what to do: if True, then do this.
num_of_people = 2
if num_of_people < 10: #If True:

    #Any indented code that comes after an if statement is called a code block
  print('Require small meeting room..') #Then do this
  print('Small TV for presentation..') #Then this


#An if statement lets us decide what to do: if False, then don’t do this
num_of_people = 11
if num_of_people < 10: #If True:
    #Because the conditional is False, this block doesn’t run
    print('Require Big Training room..') #Then do this
    print('Big Projector for presentation.') #Then this
#Nothing happens…

#The Program Continues After the Conditional
#The code continues to run as usual, line by line, after the conditional block.

num_of_people = 11
if num_of_people < 10: #If True:
    #Because the conditional is False, this block doesn’t run
    print('Require small meeting room..') #Then do this
    print('Small TV for presentation.') #Then this
print('Start python Training!') #Always this


#Rules for Whitespace in Python
#In Python, indent with 4 spaces. However, anything will work as long as you’re consistent.
num_of_people = 9
if num_of_people < 10: #If True:
    #Irregular spacing is no!
    # Block start
  print('Require small meeting room..') #2 spaces
    #print('Small TV for presentation.') #4 spaces
print('Start python Training!')
#*IndentationError: unexpected indent
#**The PEP 8 style guide recommends 4 spaces


#Conditional — if False --> else
num_of_people = 11
if num_of_people < 10: #If this statement is True, then run the indented code below
    print('Require small meeting room..') #2 spaces
else:
    print('Require Big training room..') #Otherwise, then run the indented code below
    print('Start python Training!')


#Conditionals — How to Check Another Condition
#elif Allows Checking Alternatives
num_of_people = 11
first_day_of_python_training = 'Monday'
#Else sequences will exit as soon as a statement is True…
if num_of_people < 3: #If this statement is True, then run the indented code below
    print('Require small meeting room..')
elif num_of_people == 5: # elif means otherwise if
    print('Require Medium or Large training room..')
elif first_day_of_python_training == 'Monday': # elif means otherwise if
    print('Python Training started on ', first_day_of_python_training)
else:
    print('Require Big training room..') #Otherwise, then run the indented code below


#Combining Conditionals With and/or
month_of_day = '1st May'
first_day_of_python_training = 'Wednesday'
if month_of_day == '1st May':
    print('No Python Training..')

if first_day_of_python_training == 'Wednesday':
    print('No Python Training on that day..')

#Putting 'or' in Our Program
if month_of_day == '24st April' or first_day_of_python_training == 'Wednesday':
    print('No Python Training on that day..')

#Putting 'and' in Our Program
if month_of_day == '21st May' and first_day_of_python_training == 'Wednesday':
    print('No Python Training on that day..')



#Boolean Operators — and / or
#Make it possible to combine comparisons or booleans.

#If 1 is False and result will be False

print(True and True) #True
print(True and False) #False
print(False and False) #False

#If 1 is True or result will be True
print(True or True) #True
print(True or False) #True
print(False or False) #False

#Incorporating the and / or operators
num_of_people = 11
python_training_day = 'Thursday'
#Else sequences will exit as soon as a statement is True…
if num_of_people < 3 or python_training_day == 'Thursday': #If this statement is True, then run the indented code below
    print('Require small meeting room..')
elif num_of_people >= 5 and python_training_day == 'Thursday': # elif means otherwise if
    print('Require Medium or Large training room..')
elif python_training_day == 'Thursday': # elif means otherwise if
    print('Next Python Training on ', python_training_day)
else:
    print('Require Big training room..') #Otherwise, then run the indented code below


#User Input — With the input() Function
# Ask the user to input the day of the training week
day = 'Python'
day = input('Enter the day of the training week')
#day saves the user's input
#prints out this statement and waits for user input
print('You entered training day week:', day)


##Event Test
#Receive User 2 Inputs From Console
# 1st with day of the week
# 2nd day in the month
# today_date = 26
# week_day = 'Thursday'
# print input text based int or string ie. using if and else with or / and operator
#   1st if condition print('Python training is there today..') based on or operator
#   2nd elif condition print('No Python training today..') based on and operator
#   3rd else condition print('Python training is always on Tuesday's and Thursday's in a week..')
#output: print either one of it based on the user inputs..


#Nested Conditionals
# Program checks if the number is positive or negative
# And displays an appropriate message
num = 3
# Try these two variations as well.
# num = -5
# num = 0
if num >= 0:
    print("Positive or Zero")
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        if (num % 2) == 0:
            print(num, "is a even number")
        else:
            print(num, "is not a odd number")
else:
    print("Negative number")



##Even Test Quality of the software Product
#1st level => 50 or above
#   90 or above => 'A' * Excellent Quality
#   70 or above => 'B' * Best Quality
#   50 or above => 'C' * Good Quality
#2nd level => 20 or above
#   30 or above => 'D' * Average Quality
#   20 or above => 'E' * Average Quality
#3rd level print (R* Reject) => 'R'