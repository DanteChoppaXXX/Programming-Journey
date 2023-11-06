#!../bin/python3
#prompt the user for an input

while True:
    try:
        x = int(input("enter first number: "))
        y = int(input("enter second number: "))
        sum = x + y
        print(sum)
    except (TypeError, ValueError):
        msg = "Please enter number not text."
        print(msg)