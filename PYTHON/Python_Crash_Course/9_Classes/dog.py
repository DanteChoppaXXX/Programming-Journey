#!../bin/python3

class Dog():
    """A simple attempt tot model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()}, is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name.title()}, rolled over!")
