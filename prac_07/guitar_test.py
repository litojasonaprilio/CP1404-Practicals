from prac_07.guitar import Guitar

CURRENT_YEAR = 2018


def testing():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 1512.9)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 96, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other.name, 6, other.get_age()))

    print("/n{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(other.name, False, other.is_vintage()))


testing()
