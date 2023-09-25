#!../bin/python3
import time

name = input('what is your name? : ')
password = input('password : ')

# if name == 'Kiriko':
#     print('Hello, Kiriko')
    
#     if password == 'rogueninja':
#         print('Access Granted!')
#     else:
#         print('Wrong Password')
# else:
#     print('Intruder! FUCK OFF!!!')

# A more programmatic way to write the above code
if name == 'Kiriko':
    if name == 'Kiriko' and password == 'rogueninja':
        time.sleep(0.5)
        print('ACCESS GRANTED!')
        time.sleep(1)
        print('WELCOME KIRIKO!')
    else:
        print('Wrong Password')
else:
    print('Intruder! FUCK OFF!!!')