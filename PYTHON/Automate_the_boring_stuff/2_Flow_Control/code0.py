#!../bin/python3
import time

name = input('what is your name? : ')
age = int(input('How old are you? : '))
# password = input('password : ')

# IF AND ELSE STATEMENT

# if name == 'Kiriko':
#     print('Hello, Kiriko')
    
#     if password == 'rogueninja':
#         print('Access Granted!')
#     else:
#         print('Wrong Password')
# else:
#     print('Intruder! FUCK OFF!!!')

# A more programmatic way to write the above code
# if name == 'Kiriko':
#     if name == 'Kiriko' and password == 'rogueninja':
#         time.sleep(0.5)
#         print('ACCESS GRANTED!')
#         time.sleep(1)
#         print('WELCOME KIRIKO!')
#     else:
#         print('Wrong Password')
# else:
#     print('Intruder! FUCK OFF!!!')

# ELIF STATEMENT
if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are Not Alice, kiddo')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
else:
    print('You are neither Alice nor a little kid.')

