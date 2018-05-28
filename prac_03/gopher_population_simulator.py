import random

POPULATION = 1000
MIN_BORN = 0.1
MAX_BORN = 0.2
MIN_DIED = 0.05
MAX_DIED = 0.25
YEAR_PERIOD = 10

print("Welcome to the Gopher Population Simulator!")
print("Starting population:", POPULATION, "\n")

for i in range(1, YEAR_PERIOD + 1):
    print("Year {}".format(i))
    print("*****")

    born = int(random.uniform(MIN_BORN, MAX_BORN) * POPULATION)
    died = int(random.uniform(MIN_DIED, MAX_DIED) * POPULATION)
    print("{} gophers were born. {} died.".format(born, died))

    total = POPULATION + born - died
    print("Population: {}".format(total), "\n")