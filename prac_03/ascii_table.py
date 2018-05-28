LOWER = 33
UPPER = 127


def main():
    num = get_number(LOWER, UPPER)
    print("The character for {} is {}".format(num, chr(num)))
    for value in range(LOWER, UPPER + 1):
        print("{:3} {:>3}".format(value, chr(value)))


def get_number(lower = LOWER, upper = UPPER):
    while True:
        try:
            num = int(
            input("Enter a number between {} and {}: ".format(lower, upper)))
            while num < lower or num > upper:
                print("Please enter a valid number")
                num = int(
                    input("Enter a number between {} and {}: ".format(lower, upper)))
            break
        except ValueError:
            print("Please enter a valid number")
    return num


main()