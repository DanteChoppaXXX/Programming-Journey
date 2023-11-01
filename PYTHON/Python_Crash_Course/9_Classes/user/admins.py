#!../..bin/python3
from user  import User

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