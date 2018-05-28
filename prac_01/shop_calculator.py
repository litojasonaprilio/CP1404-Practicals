number = int(input("Number of items: "))
if number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
else:
    sum = 0
    i = number
    for i in range(i, 0, -1):
        price = float(input("Price of item: "))
        sum = sum + price
if sum > 100:
    total = 0.9 * sum
else:
    total = sum
print("Total price for", number, "items is ${:.2f}".format(total))