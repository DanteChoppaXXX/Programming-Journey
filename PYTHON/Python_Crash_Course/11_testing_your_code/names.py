#!../bin/python3
from name_function import get_formatted_name as nf
print("Enter q to quit")
while True:
    first = input("What's your first name?: ")
    if first == 'q':
        break
    middle = input("What's your middle name?: ")
    if middle == 'q':
        break
    last = input("What's your last name?: ")
    if last == 'q':
        break
    

    print(f"Well Formatted Full Name: {nf(first, middle, last)}")
