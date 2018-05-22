# A set is an unordered collection with no duplicate elements

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# show that duplicates have been removed
print(basket)

# {'orange', 'banana', 'pear', 'apple'}

# fast membership testing
print('orange' in basket)
#True
print('crabgrass' in basket)
#False

 # Demonstrate set operations on unique letters from two words
...
a = set('aabbccdd')
b = set('alacazam')
c = ('werfretr')
# unique letters in a
print(a)
# -> {'a', 'r', 'b', 'd', 'c'}


basket0 = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
basket1 = {'mango', 'apple', 'pear', 'banana'}

print(basket0)
print(basket1)
print(basket0 ^ basket1)

print(a - b)
# -> {'b', 'd', 'r'}

# letters in a or b or both
print(a | b)
# -> {'a', 'm', 'r', 'l', 'b', 'd', 'z', 'c'}

# letters in both a and b
print(a & b)
# -> {'a', 'c'}

# letters in a or b but not both
print(a ^ b)
# -> {'m', 'd', 'r', 'l', 'z', 'b'}