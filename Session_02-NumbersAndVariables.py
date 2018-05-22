#addition
my_var = 3 + 5
print("Addition of (3 + 5):", my_var)

#subtraction
my_var = 10-5 #'John'#
print("Subtraction of (10-5): %d" %my_var)
#print("Subtraction of (10-5): %s" %my_var)

#multiplication
my_var = 3 * 5
print("Multiplication 3*5 : {0}".format(my_var))

#division
my_var1 = 30
my_var2 = 6
#print('Correct answer: {0:n},{1}'.format((my_var1/my_var2), my_var1))
#print('Correct answer: {:}'.format(my_var1/my_var2))
#print('Correct answer: {:%}'.format(my_var1/my_var2))
print('Correct answer: {:.2%}'.format(my_var1/my_var2))

#exponent
my_var1 = 2
my_var2 = 3

print("Square of %d = %d" %(my_var1, (my_var1**my_var2)))

#negation
my_var = -2 + -3
print(my_var)


#Integers and Floats
#int
my_var = 35
print(my_var)

#float
my_var = 30.5
print(my_var)

#Order of Operations -> 36
my_var = ( 5 + 7 ) * 3
print(my_var)

# -> 26
my_var = 5 + 7 * 3
my_var = float(3)
print(my_var)

my_var1 = my_var
my_var is my_var1

#PEMDAS: Parentheses Exponent Multiplication Division Addition Subtraction

# Division
my_var = 1450/60/3
print(my_var)

#1450/60

# Correct Order of Operations
my_var = 1450 / (60 / 3)
print(my_var)

#ceil() is short for ceiling, which rounds up
import math as m
num_parrots= 4.1
my_var = m.ceil(num_parrots)
print(my_var)