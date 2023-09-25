#!../bin/python3
import time

name = input('What is your name? : ')
clan = input('What clan do you belong? :')

if name == 'Sasori':
    print('WELCOME, GREAT PUPPET MASTER!')
elif clan != 'Akatsuki':
    print('You Do not Belong Here!')
elif clan == 'Uchiha':
    print('Kill Him!!!')
else:
    print('Leave Now, Shinobis Only!')

