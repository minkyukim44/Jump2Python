## Variables

a = [1,2,3]
id(a)               # check memory address of a

b = a
b
id(a)
id(b)               # a and b are identical
a is b
a[1] = 4
a
b 

a = [1,2,3]
b = a[:]            # slicing
a[1] = 4
a
b                   # a and b are different

from copy import copy       # use a function, 'copy'
a = [1,2,3]
b = copy(a)
a 
b 
b is a              # a and b are different

a, b = ('python','life')
(a,b) = 'python','life'
[a,b] = ['python','life']
a = b = 'python'

a = 3
b = 5
a, b = b, a         # exchange
a
b

a = [1,2,3]
b = [1,2,3]
a is b              # different memory addresses