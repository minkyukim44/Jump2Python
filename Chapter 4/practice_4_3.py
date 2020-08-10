## read and write a file
# generate a file
f = open("nfile.txt",'w')       # 'w': writing mode / 'r': reading mode / 'a': adding mode
f.close()

f = open("C:/Users/MK/Desktop/Programming/Jump2Python/Chapter 4/nfile.txt", 'w')
for i in range(1,11):
    data = "It is the %dth row.\n" % i
    f.write(data)
f.close()

# 'readline()'
f = open("C:/Users/MK/Desktop/Programming/Jump2Python/Chapter 4/nfile.txt", 'r')
line = f.readline()     # read the first line
print(line)
f.close()

f = open("C:/Users/MK/Desktop/Programming/Jump2Python/Chapter 4/nfile.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 'readlines()'
f = open("C:/Users/MK/Desktop/Programming/Jump2Python/Chapter 4/nfile.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# 'read()'
f = open("C:/Users/MK/Desktop/Programming/Jump2Python/Chapter 4/nfile.txt", 'r')
data = f.read()
print(data)
f.close()

# add data
f = open("C:/Users/MK/Desktop/Programming/Jump2Python/Chapter 4/nfile.txt", 'a')
for i in range(11,20):
    data = "It is the %dth row.\n" % i
    f.write(data)
f.close()

# use 'with'
f = open("C:/Users/MK/Desktop/Programming/Jump2Python/Chapter 4/foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

with open("C:/Users/MK/Desktop/Programming/Jump2Python/Chapter 4/foo.txt","w") as f:
    f.write("Life is too short, you need python")
