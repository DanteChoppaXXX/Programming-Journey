#!../bin/python3
import time

#This program says Hello and asks for my name
time.sleep(2)
print('====================AKATSUKI RISING====================\n')
time.sleep(1)
print('Hello, Human!\n')
time.sleep(1)
#Ask for the user's name
print('What is your name?')
userName = input()
print("It's good to meet you, " + userName)
time.sleep(1)
print('The length of your name is =', len(userName),'figures')
# print(len(userName))
#Ask for the user's age
print('\nWhat is your age?')
userAge = input()
time.sleep(1)
future = 'You will be ' + str(int(userAge) + 1) + ' in a year'
print(future)
print('Total number of characters in the previous sentence is', len(future))