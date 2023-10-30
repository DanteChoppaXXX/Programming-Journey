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

class Privileges():
    """Creating a class for privileges"""
    def __init__(self, privileges):
        """Create list of admin privileges"""
        privileges = ['can add post', 'can delete post', 'can ban users', 'can add users', 'can mute chatroom']
        self.privileges = privileges

    def show_privileges(self):
        """Display all Administrator's privileges."""
        print('ADMIN PRIVILEGES\n================')        
        for i, privilege in enumerate(self.privileges, 1):
            print(f'{i}: {privilege}')


class Admin(User):
    """Creating an Admin user."""
    def __init__(self, first_name, last_name, username, email, privileges):
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges(privileges)


admin0 = Admin('kath', 'carl', 'katty', 'kath@email.com', 'privileges')
admin0.privileges.show_privileges()
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
