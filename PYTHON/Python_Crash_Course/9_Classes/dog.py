#!../bin/python3

class Dog():
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name.title()} rolled over!")


my_dog = Dog('Jack', 7)
your_dog = Dog('Miles', 6)

print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()

print(f"Your dog's name is {your_dog.name.title()}.")
print(f"Your dog is {your_dog.age} years old")
your_dog.sit()


# keep_going = True
# while keep_going:
#     name = input("What's your dog's name? ")
#     age = int(input("How old is your dog? "))

#     my_dog = Dog(name, age)

#     print(f"My dog's name is {my_dog.name.title()}.")
#     print(f"{my_dog.name} is {my_dog.age} years old.\n")

#     my_dog.sit()
#     my_dog.roll_over()

#     moreDogs = input("Do you have another dog? (y or n) :")
#     if moreDogs == "n":
#         keep_going = False

