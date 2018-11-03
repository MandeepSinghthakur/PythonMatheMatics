#A Set, s, is a subset of another set,t , if all the memebers of s are also members of t

from sympy import FiniteSet

s = FiniteSet(1)
t = FiniteSet(1,2)
print(s.is_subset(t))
print(t.is_subset(s))

#Note - Empty set is a subset of every Set

#Similary, a set ,t, is said to be a superset of another set, s, if t contains all of the members contained in s
# You can check Wheather one set is a superset of another using the is_superset Method

# The Power set of a set is the set of all the possible subsets of s. ANy set ,s, has precisely 2^|s|
# subsets , where |s| is the cardinality of the set. For example, the set {1, 2, 3} has a cardinality
# of 3, so it has 2^3 or 8 subsets
# We can find the power set using powerset() method
s = FiniteSet(1,2,3)
ps = s.powerset()
print(ps)