#!..bin/python3

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        
    if number % 2 == 1:
        print(3 * number + 1)

try:
    collatz(int(input('Enter Number: ')))

except ValueError:
        print('You must enter an integer')
