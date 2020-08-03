## for statement
# example - 1
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

# example - 2 
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

# example - 3
marks = [90, 25, 67, 45, 80] 
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("The %dth student is passed" % number)
    else:
        print("The %dth student is failed" % number)

# example - 4
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print("Congratulation, you, %dth student, are passed" % number)

# example - 5
a = range(10)       # 0 ~ 9
a
a = range(1,11)     # 1 ~ 10
a

add = 0
for i in range(1,11):
    add = add + i

print(add)

# example - 6
marks = [90, 25, 67, 45, 80]
range(len(marks))
for number in range(len(marks)):
    if marks[number] < 60: continue
    print(("Congratulation, you, %dth student, are passed" % (number + 1))

add = 0
for i in range(1,101):
    add = add + i

# example - 7
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end = "")        # end = "" : do not change the row 
    print('')                       # change the row

# example - 8
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

result1 = [num*3 for num in a]
print(result1)

result2 = [num*3 for num in a if num % 2 == 0]
print(result2)

result3 = [x*y for x in range(2,10)
    for y in range(1,10)]
