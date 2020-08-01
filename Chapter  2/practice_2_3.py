## Practice "List"

odd = [1,3,5,7,9]
e = [1,2,['Life','is']]

a = [1,2,3]
a[0]
a[0] + a[2]
a[-1]

a = [1,2,3,['a','b','c']]
a[-1][0]
a[-1][1]

a = [1,2,['a','b',['Life','is']]]
a[2][2][0]

a = [1,2,3,4,5]
a[0:2]          # 0 <= i <2
a[:2]
a[2:]
a[1:3]

a = [1,2,3,['a','b','c'],4,5]
a[3][:2]

a = [1,2,3]
b = [4,5,6]
a + b
a * 3
len(a)
a[2] + 'hi'     # error
str(a[2]) + 'hi'
a[2] = 4        # change an element
del a[1]        # delete an element

a = [1,2,3,4,5]
del a[2:]

a = [1,2,3]
a.append(4)     # add the fourth element
a.append([5,6])

a = [1,4,3,2]
a.sort()        

a = ['a','c','b']
a.sort()
a.reverse()     # reverse the current order

a = [1,2,3]
a.index(3)      # show the third element, no 0th element
a.insert(0,4)   # insert '4' at the 0th location
a.insert(3,5)

a = [1,2,3,1,2,3]
a.remove(3)     # remove the very first '3'

a = [1,2,3]
a.pop()         # return the last element, and delete it
a.pop(1)        # return the first location element, and delete it

a = [1,2,3,1]
a.count(1)      # count '1's in the list

a = [1,2,3]
a.extend([4,5])
b = [6,7]
a.extend(b)
a += [8,9]      # i += 1 <=> i = i + 1