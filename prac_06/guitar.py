# Design a Guitar class.

CURRENT_YEAR = 2021
VINTAGE_AGE = 50


# Guitar class to store guitar details.
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """2f format specifier to achieve (Gibson L-5 CES (1922) : $16,035.40)"""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        return CURRENT_YEAR - self.year  # Using current year get age of the guitar.

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE  # Determine if the guitar is vintage or not

    def __lt__(self, other):
        return self.year < other.year  # Sort guitars by the year they are released
