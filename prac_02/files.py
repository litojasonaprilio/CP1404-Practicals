OUTPUT_FILE = "name.txt"

# 1
output_file = open(OUTPUT_FILE, 'w')
name = input("Enter your name: ")
print(name, file=output_file)
output_file.close()

# 2
input_file = open(OUTPUT_FILE, 'r')
print("Your name is", name)
input_file.close()

# 3
input_file = open('numbers.txt', 'r')
num1 = int(input_file.readline())
num2 = int(input_file.readline())
print(num1 + num2)
input_file.close()

# 4 extended
input_file = open('numbers.txt', 'r')
total = 0
for line in input_file:
    number = int(line)
    total += number
print(total)
input_file.close()