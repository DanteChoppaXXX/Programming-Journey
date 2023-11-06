#!../bin/python3
import json

numbers = [1, 3, 4, 6, 7, 8, 9]

# filename = "numbers.json"
# with open(filename, 'w') as file:
#     json.dump(numbers, file)

def get_stored_user():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as file:
                userName = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return userName

def get_new_user():
    username = input("What's your name? ")
    user = username.title()
    filename = 'username.json'
    with open(filename, 'w') as file:
        json.dump(user, file)
        print(f"We'll remember you when you come back, {user}")

def greet_user():
    """Greet the user by name."""
    userName = get_stored_user()
    if userName:
        print(f"Welcome back {userName}")
    else:
        get_new_user()   

greet_user()

# with open(filename) as file:
#     number = json.load(file)
#     print(number)