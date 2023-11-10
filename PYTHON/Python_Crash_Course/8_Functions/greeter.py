#!../bin/python3

# #Exercise 1
# def display_message():
#     """Tell everyone what you're learning."""
#     message = 'I am learning about functions in Python'
#     print(message)

# display_message()

# #Exercise 2
# def favorite_book(title):
#     """Tell what your favorite book is."""
#     message = f'One of my favorite books is {title}'
#     print(message)

# favorite_book('Alice in Wonderland')

#PASSING A LIST TO A FUNCTION!!!
def greet_users(names):
    """Print a greeting to all users in the list."""
    for i, name in enumerate(names, start=1):
        msg = f'{i}. Hello, {name.title()}!'
        print(msg)

users = ['kate', 'john', 'chan', 'sasori']
greet_users(users)
