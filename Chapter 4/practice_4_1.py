## functions
def add(a,b):
    return a+b

a = 3
b = 4
c = add(a, b)
print(c)
print(add(3, 4))
print(add(a=3, b=7))
print(add(b=7, a=3))

def say():
    return 'Hi'

def add1(a,b):
    print("The sum of %d and %d is %d" % (a, b, a+b))

def say1():
    print('Hi')

# multiple inputs
def add_many(*args):                # '*' makes a tuple with all inputs
    result = 0
    for i in args:
        result = result + i
    return result

add_many(1,2,3,4,5,6,7,8,9,10)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

print(add_mul('add', 1,2,3,4,5))
print(add_mul('mul', 1,2,3,4,5))

# make a dictionary form
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo',age=3)

# each function has only one output
# do not use 'return' more than one time
def add_and_mul(a,b):
    return a+b, a*b         

result = add_and_mul(3,4)
result1, result2 = add_and_mul(3,4)
result1
result2

# method for escaping a function
def say_nick(nick):
    if nick == "idiot":
        return
    print("My nickname is %s" % nick)

say_nick('yahoo')
say_nick('idiot')