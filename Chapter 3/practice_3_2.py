## while statement
# example - 1
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("Hit the tree in %d times." % treeHit)
    if treeHit == 10:
        print("The tree fell.")

# example - 2
prompt = """
1. Add
2. Del
3. List
4. Quit
Enter the number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())

# example - 3
coffee = 10
money = 300
while money:
    print("Give a coffee after paying")
    coffee = coffee -1
    print("%d cups of coffee are left." % coffee)
    if coffee == 0:
        print("Unavailable due to no more coffee left.")
        break
coffee = 10
while True:
    money = int(input("Put your money: "))
    if money == 300:
        print("Give a cup of coffee.")
        coffee = coffee - 1
    elif money > 300:
        print("Give a change, %d, and give a cup of coffee." % (money - 300))
        coffee = coffee -1
    else:
        print("Give the money back and do not give a cup of coffee.")
        print("%d cups of coffee are left." % coffee)
    if coffee == 0:
        print("No more coffee, Stop selling.")
        break

# example - 4
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue  # bring it back to the condition line
    print(a)

# example - 5
while True:
    print("Push Ctrl+C and then escape from the while-statement")