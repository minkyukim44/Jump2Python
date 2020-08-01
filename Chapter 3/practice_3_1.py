## if statements

money = True
if money:
    print("Take a taxi")
else:
    print("Take a walk")
    
money = 2000
if money >= 3000:
    print("Take a taxi")
else:
    print("Take a walk")

money = 2000
card = True
if money >= 3000 or card:
    print("Take a taxi")
else:
    print("Take a walk")

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("Take a taxi")
else:
    print("Take a walk")

if 'card' in pocket:
    print("Take a bus")
else:
    print("Take a walk")

# do nothing
if 'money' in pocket:
    pass
else:
    print("Take out a card")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("Take a taxi")
elif card:
    print("Take a taxi")
else:
    print("Take a walk")

score = 70
message = "success" if score >= 60 else "failure"
print(message)