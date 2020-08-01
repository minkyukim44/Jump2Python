a=123
print(a)

octal=0o177     #8진법
print(octal)

7/4             #나누기
7//4            #나눈 몫 반환

# 문자열 만들기
"Hello World"

'Python is fun'

"""Life is too short, You need python"""

'''Life is too short, You need python'''

# 문자열에 작은 따옴표, 큰 따옴표 포함시키기
food = "Python's favorite food is perl"
food

say = '"Python is very easy." he says.'
say

food_1 = 'Python\'s favorite food is perl'
food_1
say_1 = "\"Python is very easy.\" he says."
say_1

# 여러 줄인 문자열
multiline = "Life is too short\nYou need python"
multiline
print(multiline)

multiline_1 = '''
Life is too short
You need python
'''
multiline_1
print(multiline_1)

multiline_2 = """
Life is too short
You need python
"""
multiline_2
print(multiline_2)

# 문자열 연산하기
head = "Python"
tail = " is fun!"
head + tail

a = "python"
a * 2

# 문자열 길이 구하기
a_1 = "Life is too short"
len(a_1)

# 문자열 인덱싱과 슬라이싱
a_2 = "Life is too short, You need Python"
a_2[3]      # python counts a number from 0
a_2[0]
a_2[-1]

b = a_2[0] + a_2[1] + a_2[2] + a_2[3]   #slicing
b

a_2[0:4]        # 0 <= a_2 < 4
a_2[0:5]
a_2[19:]
a_2[:]
a_2[19:-7]

a_3 = "20010331Rainy"

date = a_3[:8]
weather = a_3[8:]
date
weather

year = a_3[:4]
day = a_3[4:8]
year
day

sample = "Pithon"
sample_fix = sample[0] + 'y' + sample[2:]
sample_fix