## Pracitce Sets

s1 = set([1,2,3])
s1

s2 = set("Hello")       # unordered, non-overlapped, non-indexing
s2

# change to a list and a tuple
s1 = set([1,2,3])
s1[0]                   # error

l1 = list(s1)
l1
l1[0]

t1 = tuple(s1)
t1
t1[0]

# operators for sets
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

s1 & s2     # intersection
s1.intersection(s2)

s1 | s2     # union
s1.union(s2)

s1 - s2     # difference
s2 - s1
s1.difference(s2)
s2.difference(s1)

# functions for sets
s1 = set([1,2,3])
s1.add(4)           # add an element
s1

s1 = set([1,2,3])
s1.update([4,5,6])  # add more than one element
s1

s1 = set([1,2,3])
s1.remove(2)        # remove an element
s1