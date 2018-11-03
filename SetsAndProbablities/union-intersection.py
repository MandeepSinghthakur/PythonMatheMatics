# Set Operations  such as Union, Intresection and the cartesian product allow you to
# combine sets in certain methodical ways. These set operations are extremely useful in real world
# Problem solving situations when we have to consider multiple sets together.

from sympy import FiniteSet
s = FiniteSet(1,2,3)
t = FiniteSet(2,4,6)
#The result is the third set with all the distinct  members of the two sets
print(s.union(t))
 

# The intersection of two sets creates a new set from the elelments common to both sets
# For Example, the intersection of the sets {1,2} and {2,3} will result in a new set with the only common element 2.
s = FiniteSet(1,2)
t = FiniteSet(2,3)
print(s.intersect(t))

# Whereas the union operation finds memebers that are in one set or another,
# the intersection operation finds elements that are present in both.Both of these operations
# can also be applied to more than two sets. For Example- here's how you'd find the union of three sets

s = FiniteSet(1,2,3)
t = FiniteSet(2,4,6)
u = FiniteSet(3,5,7)

print(s.union(t).union(u))


# CARTESIAN PRODUCT
# The cartesian product of two sets creates a set that consist all the possible pairs made by taking
# an element from each set. For examples cartesian product of the sets {1,2} and {3,4} is {(1,3),(1,4),(2,3),(2,4)}
# In SymPy you can find the cartesian product of two sets by simply using the multiplication operator
p = s * t
print(p)