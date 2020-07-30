# Q1
a = [80, 75, 55]
sum(a)/3

# Q2
13 % 2

# Q3
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# Q4
print(pin[7])

# Q5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# Q6
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# Q7
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

# Q8
a = (1, 2, 3)
a = a + (4,)
print(a)

# Q10
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

# Q12
a = b = [1, 2, 3]
a[1] = 4
print(b)