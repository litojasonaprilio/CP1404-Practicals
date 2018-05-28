"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 17.5%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $100, or falls below $1, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

MAX_INCREASE = 0.175  # 17.5% # changed
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1 # changed
MAX_PRICE = 100.0 # changed
INITIAL_PRICE = 10.0
OUTPUT_FILE = "stock_output.txt"

out_file = open(OUTPUT_FILE, 'w') # changed

price = INITIAL_PRICE
print("Starting price: ${:,.2f}".format(price), file=out_file)
i = 0

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_INCREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    i += 1
    print("On day {0} price is: ${1:,.2f}".format(i, price), file=out_file)

out_file.close()