x = int(input("Enter smaller number: "))
y = int(input("Enter bigger number: "))

MENU = """1. Show the even numbers from x to y
2. Show the odd numbers from x to y
3. Show the squares from x to y
4. Exit the program"""
print(MENU)

choice = input(">>> ").upper()
while choice != "4":
    if choice == "1":
        for i in range(x, y + 1):
            if i%2 == 0:
                print(i, end=' ')
    elif choice == "2":
        for i in range(x, y + 1):
            if i%2 == 1:
                print(i, end=' ')
    elif choice == "3":
        for i in range(x, y + 1):
            if (int(i ** 0.5)) ** 2 == i:
                print(i, end=' ')
    else:
        print("Invalid choice")
    print()
    print(MENU)
    choice = input(">>> ").upper()

print("Thank You and Goodluck")