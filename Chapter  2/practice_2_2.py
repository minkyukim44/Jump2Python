## String Formatting

# Insert an integer (%d)
"I eat %d apples." % 3

# Insert a string (%s)
"I eat %s apples." % "five"
"rate is %s." % 3.234       # for floating-point, have to use %f. but in this case, 3.234 is converted as a string. 

# Insert a variable
number = 3
"I eat %d apples." % number

# Insert more than one
number = 10
number1 = 3
day = "three"
"I ate %d apples. so I was sick for %s days and %d months" % (number, day, number1)

# etc
"Error is %d%%." % 98   # for "%", should use "%%".

# Show blank
"%10s" % "hi"       # start at 10 points right.
"%-10sjane" % "hi"  # start at 10 points left.

# Express floating-point
"%0.4f" % 3.42134234    # show till 4th digit
"%10.4f" % 3.42134234   # w/ blank

# use "format" function
"I eat {0} apples".format(3)
"I eat {0} apples".format("five")
number = 3
"I eat {0} apples". format(number)
number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)
"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)

"{0:<10}".format("hi")      # left arrangement
"{0:>10}".format("hi")      # right arrangement
"{0:^10}".format("hi")      # middle arrangement
"{0:=^10}".format("hi")     # fill the blank 
"{0:!<10}".format("hi")

y = 3.42134234
"{0:0.4f}".format(y)
"{0:10.4f}".format(y)

"{{ and }}".format()        # express "{ and }"

# 'f' string formmating
name = "홍길동"
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
f'나는 내년이면 {age+1}살이 된다.'

d = {'name':'홍길동','age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'

f'{"hi":<10}'
f'{"hi":>10}'
f'{"hi":^10}'
f'{"hi":=^10}'
f'{"hi":!<10}'

y = 3.42134234
f'{y:0.4f}'
f'{y:10.4f}'

f'{{ and }}'

f'{"python":!^12}'
"{0:!^12}".format("python")

## About character

a = "hobby"
a.count('b')        # count 'b' in 'hobby'

a = "Python is the best choice"
a.find('b')         # find the location where 'b' is
a.find('k')         # the letter 'k' does not exist (-1)

a = "Life is too short"
a.index('t')        # find the location where 't' is
a.index('k')        # the letter 'k' does not exist (error)

",".join('abcd')    # insert "," between each letter
",".join(['a','b','c','d'])

a = "hi"
a.upper()           # capitalize letters

a = "HI"
a.lower()           # de-capitalize letters

a = " hi "
a.lstrip()          # remove spaces on the left side
a.rstrip()          # remove spaces on the right side
a.strip()           # remove spaces on the both sides

a = "Life is too short"
a.replace("Life", "Your leg")       # replace phrases
a.split()                           # divide characters by spaces

b = "a:b:c:d"
b.split(':')                        # divide characters by ':'


