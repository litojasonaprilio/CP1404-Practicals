import random

NUMBERS_IN_LINE = 6
MIN = 1
MAX = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 1:
        print("Invalid Number")
        quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        quick_picks = []
        for j in range(NUMBERS_IN_LINE):
            number = random.randint(MIN, MAX)
            while number in quick_picks:
                number = random.randint(MIN, MAX)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join("{:2}".format(number) for number in quick_picks))


main()