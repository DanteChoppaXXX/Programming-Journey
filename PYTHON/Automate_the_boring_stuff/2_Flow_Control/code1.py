#!../bin/python3
import time
import random

# name = input('What is your name? : ')
# clan = input('What clan do you belong? :')

# while name == 'Sasori':
#     print('WELCOME, GREAT PUPPET MASTER!')

# digit = 3

# while digit < 5:
#     print('Hack The World!!!')
#     digit = digit + 1
    
# An Annoying Loop
# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     name = input()
# print('Thank You!')

# coin_side0 = 'Head'
# coin_side1 = 'Tail'
print('===== WELCOME =====')
time.sleep(1)
input('Press Enter To Continue')
time.sleep(0.5)
print('=========> TOSS DA COIN <==========')
print("Loading.", end="")
time.sleep(1)
print(".", end="") 
time.sleep(1) 
print(".")

time.sleep(3)
while True:
#Simulate a coin toss where (0 is for Head and 1 is for Tail)
    toss = random.randint(0,1)
    choice = input('Head or Tail? : ')
    choice = choice.lower()
    if choice == 'head' or choice == 'tail':
        time.sleep(3)
        print(f"Result:{'Head' if toss == 0 else 'Tail'}")
        break
    else:
        print('Try again!')
            

