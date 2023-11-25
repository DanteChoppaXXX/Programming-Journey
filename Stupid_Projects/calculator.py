#!./env/bin/python3
""" Build a basic calculator that can perform operations like addition, subtraction, multiplication, and division. You can take user input for numbers and the operation to perform."""
# Give your user a personalized experience.
# Ask the user for their name.
name = input("What's your name?: ")

# Give the user ownership of the calculator by assigning their name to it
owner = f"{name.upper()}'S CALCULATOR"
owner_len = len(owner)      # Get the length of the message characters.
print(owner)        # Display the message.
print(owner_len * '=')      # Display a decorator equal to the length of the displayed message.

# Get the user input
x = float(input("Enter first number: "))
operator = input("Choose maths operator[+, -, /, *]: ")
y = float(input("Enter second number: "))

# Make the calculator
def add():
    add_up = x + y
    print(add_up)

def subtract():
    minus = x - y
    print(minus)

def divide():
    division = x / y
    print(division)

def multiply():
    times = x * y
    print(times)

def main():
    if operator == '+':
        add()
    elif operator == '-':
        subtract()
    elif operator == '/':
        divide()
    elif operator == '*':
        multiply()
    else:
        print("Choose a valid math operator next time. e.g: [+, -, /, *]")

if __name__ == "__main__":
    main()