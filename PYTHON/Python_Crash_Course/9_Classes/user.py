#!../bin/python3

class User():
    """Creating a user profile"""
    def __init__(self, first_name, last_name, username, email):
        self.firstname = first_name
        self.lastname =last_name
        self.username = username
        self.email = email

    def describe_user(self):
        print("USER PROFILE")
        print("============")
        print(f"First Name: {self.firstname.title()}\nLast Name: {self.lastname.title()}\nUsername: {self.username}\nEmail Address: {self.email}")

    def greet_user(self):
        print("_______________________")
        print(f"WELCOME {self.username}")
        print("_______________________\n")

firstName = input("Enter your fist name: ")
lastName = input("Enter your last name: ")
username = input("Enter your username: ")
email = input("Enter your email address: ")

user0 = User(firstName, lastName, username, email)
user0.greet_user()
user0.describe_user()
