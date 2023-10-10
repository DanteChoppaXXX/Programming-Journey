#!..bin/python3

def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    if number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

try:
    print('Enter Number: ')
    number = int(input())
    
    while number != 1:
        number = collatz(number)

except ValueError:
        print('You must enter an integer')
