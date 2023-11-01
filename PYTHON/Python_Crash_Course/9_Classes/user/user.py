#!../bin/python3

class User():
    """Creating a user profile"""
    def __init__(self, first_name, last_name, username, email):
        self.firstname = first_name
        self.lastname =last_name
        self.username = username
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print("USER PROFILE")
        print("============")
        print(f"First Name: {self.firstname.title()}\nLast Name: {self.lastname.title()}\nUsername: {self.username}\nEmail Address: {self.email}")

    def greet_user(self):
        print("_______________________")
        print(f"WELCOME {self.username}")
        print("_______________________\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# firstName = input("Enter your fist name: ")
# lastName = input("Enter your last name: ")
# username = input("Enter your username: ")
# email = input("Enter your email address: ")

# user0 = User(firstName, lastName, username, email)
#user0.greet_user()
#user0.describe_user()
# user0 = User('kath', 'carl', 'katty', 'kath@email.com')

# user0.increment_login_attempts()
# user0.increment_login_attempts()
# user0.increment_login_attempts()
# print(f"Login Attempts: {user0.login_attempts}")

# user0.reset_login_attempts()
# print(f"Login Attempts (after reset): {user0.login_attempts}")
