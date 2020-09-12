"""CP1404: This is a program which creates a simple class, ProgrammingLanguage"""


class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """Constructs a programming language with the given inputs"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Returns information about the programming language instance"""
        return "{}, {} typing, Reflection = {}, first appeared in {}".format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        """Determine if the language has static or dynamic typing"""
        return self.typing == "Dynamic"
