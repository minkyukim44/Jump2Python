## Q1
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
        
## Q2
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)

## Q3
input1 = input("Put the first number:")
input2 = input("Put the second number:")

total = int(input1) + int(input2)
print("The sum of the two numbers is %s" % total)

## Q5
f1 = open("C:/Users/MK/Desktop/Programming/Jump2Python/Chapter 4/test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("C:/Users/MK/Desktop/Programming/Jump2Python/Chapter 4/test.txt", 'r')
print(f2.read())

## Q6 
user_input = input("Saving contents:")
f = open("C:/Users/MK/Desktop/Programming/Jump2Python/Chapter 4/test.txt", 'a')
f.write(user_input)
f.write("\n")
f.close()

## Q7
f1 = open("C:/Users/MK/Desktop/Programming/Jump2Python/Chapter 4/test.txt", 'w')
f1.write("Life is too short\n")
f1.write("you need java")
f1.close()

f = open("C:/Users/MK/Desktop/Programming/Jump2Python/Chapter 4/test.txt", 'r')
body = f.read()
f.close()

body = body.replace("java", "python")

f = open("C:/Users/MK/Desktop/Programming/Jump2Python/Chapter 4/test.txt", 'w')
f.write(body)
f.close()