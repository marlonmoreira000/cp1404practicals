"""This program creates the Guitar class"""


CURRENT_YEAR = 2020
VINTAGE_AGE = 50


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """Constructs guitar class with the following attributes"""
        self.name = name  # str
        self.year = year  # int
        self.cost = cost  # float

    def __str__(self):
        """Returns basic information about the guitar"""
        return "{} ({}): ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get the age of the guitar"""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Check if the guitar is vintage (True) or not (False)"""
        return self.get_age() >= VINTAGE_AGE

