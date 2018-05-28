LOWER = 33
UPPER = 127

MIN_COLUMNS = 2
MAX_COLUMNS = 24

char = input("Enter a character: ")
print("The ASCII code for {} is {}".format(char, ord(char)))

num = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
while num < LOWER or num > UPPER:
    print("The number must be between {} and {}.".format(LOWER, UPPER))
    num = int(input("Enter a number between {} and {}: ").format(LOWER, UPPER))
print("The character for {} is {}".format(num, chr(num)))

for value in range(LOWER, UPPER + 1):
    print("{:3} {:>3}".format(value, chr(value)))

# challenge
columns = int(input("Enter how many columns: "))
while columns < MIN_COLUMNS or columns > MAX_COLUMNS:
    print("Number of columns is {} to {}.".format(MIN_COLUMNS, MAX_COLUMNS))
    columns = int(input("Enter how many columns: "))
number_of_values = UPPER - LOWER + 1
rows = number_of_values // columns

# horizontal to vertical
value = LOWER
for row in range(rows):
    for column in range(columns):
        print("{:6} {:>2}".format(value, chr(value)), end="")
        value += 1
    print()

starting_value = value
for value in range(starting_value, UPPER + 1):
    print("{:6} {:>2}".format(value, chr(value)), end="")
print("\n")

# vertical to horizontal
for row in range(rows + 1):
    starting_value = LOWER + row
    value = starting_value
    for column in range(columns - 1):
        value_to_print = value + (column * rows)
        print("{:6} {:>2}".format(value_to_print, chr(value_to_print)), end="")
        value += 1

    value_to_print = value + ((column + 1) * rows)
    if value_to_print <= UPPER:
        print("{:6} {:>2}".format(value_to_print, chr(value_to_print)), end="")
    print()