# A tuple is a sequence of immutable Python objects
tup1 = ('Banana', 'Cherry', 2015, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
tup2 = 1, 2, None, 3, 4, 5;

# empty tuple
tup1 = ();

# single value you have to include a comma
tup1 = (50,);
tup1 = 50

# Accessing Values in Tuples
tup1 = ('Banana', 'Cherry', 2015, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print('tup1[0]: ', tup1[0]);
print('tup2[1:5]: ', tup2[1:5]);

# tup1[-1]:  Banana
# tup2[1:5]:  (2, 3, 4, 5)

# Updating Tuples
# Tuples are immutable which means you cannot update or change the values of tuple elements.

tup1 = (1223, 3412.56);
tup2 = ('Banana', 'Cherry');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup1 = tup1 + tup2;
print(tup1);

#(12, 34.56, 'abc', 'xyz')


# Delete Tuple Elements
# Removing individual tuple elements is not possible

tup = ('Banana', 'Cherry', 2015, 2000);
print(tup);
del tup;
print('After deleting tup : ');
#print(tup);


# + and * operators much like strings
#Length
len((1, 2, 3)) # -> 3

#Concatenation
(1, 2, 3) + (4, 5, 6) # ->(1, 2, 3, 4, 5, 6)

#Repetition
#('Hello!',) * 4
('Hello!', 'Hello!', 'Hello!', 'Hello!')

#Membership
3 in (1, 2, 3) # -> True
3 not in (1, 2, 3) # -> False

# Iteration
for x in (1, 2, 3):
    print(x)

# 1 2 3

# Indexing, Slicing, and Matrixes
tup = ('Banana', 'Cherry', 2015, 2000);

print(tup[2])
print(tup[-2])
print(tup[1:])
