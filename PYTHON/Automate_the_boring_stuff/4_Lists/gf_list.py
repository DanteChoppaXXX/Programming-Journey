#!../bin/python3

loml = ['Ngozi', 'Fathia', 'Amanda', 'Favour', 'Titi', 'Vee']

name = [['Daniel', 'David', 'John', 'Jack'], ['Jane', 'Kate', 'Kath', 'Titi']]

if 1 == 1:
    print(loml[-2:-6], loml[-6])
else:
    print(name[0][1], name [1][3])

print(len(name) + len(loml))
al = name + loml
del al

print(al)