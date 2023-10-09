#!../bin/python3

# def hello():
#     print('Howdy!')
#     print('Howdy!!!')
#     print('Hello there.')

# hello()
# hello()
# hello()

# def hello(name):
#     print('Hello, ' + name)

# hello('Alice')
# hello('Bob')

# def sayHello(name):
#     print('Hello, ' + name)

# sayHello('Sasori')

# print('Hello', end=' ')
# print('World')

# print('cats', 'dogs', 'mice', sep='!= ')

#Local Variables Cannot Be Used in the Global Scope
# def spam():
#     eggs = 31337

# spam()
# print(eggs)

#Local Scopes Cannot Use Variables in Other Local Scopes
# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)

# def bacon():
#     ham = 101
#     eggs = 0

# spam()

#Global Variables Can Be Read from a Local Scope
# def spam():
#     print(eggs)

# eggs = 42
# spam()
# print(eggs)

#Local and Global Variables with the Same Name
# def spam():
#     eggs = 'spam local'
#     print(eggs)     #prints 'spam local'

# def bacon():
#     eggs = 'bacon local'
#     print(eggs)     #prints 'bacon local'
#     spam()
#     print(eggs)     #prints 'bacon local'

# eggs = 'global'
# bacon()
# print(eggs)         #prints 'global'

#The global Statement
def spam():
    global eggs
    eggs = 'spam'

def nala():
    global rat
    rat = 'kill'

def heck():
    print(eggs)

rat = 'save'
eggs = 'global'
heck()
spam()
nala()

print(eggs)
print(rat)