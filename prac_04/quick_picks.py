"""
Each line (quick pick) should not contain any repeated number.
Each line of numbers should be displayed in sorted (ascending) order.
"""

import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    quick_picks = int(input("How many quick picks? "))
    while quick_picks < 0:
        print("Not a valid input.")
        quick_picks = int(input("How many quick picks? "))

    """Uses a random generated number to print numbers between 1-45"""
    for i in range(quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
