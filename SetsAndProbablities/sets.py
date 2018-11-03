# A set is a collection of distinct  objects, often called elements or members.
# Two characterstics of a set make it diffrent from just any collection of objects.
# A set is 'well-defined', meaning the question "Is a particular object in this collection"
# A set can contain anything - numbers,people,things,words and so on.

##Set Construction
# In Mathematical notation, you represent a set by writing the set members enclosed in a curly brackets
# For Example , [2, 4, 6] represent a set with 2, 4 and 6 as its members.
# To create a set in python, we can use the FiniteSet class from sympy package, as follows

from sympy import FiniteSet
s = FiniteSet(2, 4, 6)
print(s)

##Checking wheather a Number Is in a Set
print(4 in s)


#Creating Sets from Lists or tuples
members = [1,2,3]
s = FiniteSet(*members)
print(s)

#Set repetiton and Order
# Sets in python(like mathematical sets) ignore any repeats of a member , and they don't keep track
# of the order of a set memebers. For examples if you create a set from a list that has multiple
# instances of an number, the number is added to the set only once, and other instances are discarded

members = [1,2,3,2]
print(FiniteSet(*members))

# NOTE - lists and tuples have index or order in which they are saved but sets have no particular order
