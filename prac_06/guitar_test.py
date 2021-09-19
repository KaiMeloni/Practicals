# Using the guitar class test outputs  of the functions
from prac_06.guitar import Guitar

CURRENT_YEAR = 2021


def test():
    name = "Gibson L-5 CES"
    year = 1922  # 2021 therefore output will be 99 years
    cost = 16035.40
    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 1512.9)  # Output will be 9 years

    # Print sample output given with correct formatting
    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 98, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other.name, 7, other.get_age()))
    print("\n{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(other.name, False, other.is_vintage()))


if __name__ == '__main__':
    test()
