#!../../bin/python3

to_do_items = []

print('=*=*=*= TO-DO MASTER =*=*=*=')

while 1:
    print("MENU")
    print("Choose An Option")
    print("1: Add A Tasks\n2: View Tasks\n3: Mark Tasks As Done\n4: Remove A Task\n0: Quit Program")
    menu = {1:'Add A Tasks', 2:'View Tasks', 3:'Mark Tasks As Done', 4:'Remove A Task', 0:'Quit Program'}
    option = input()
    
    if option == 1:
        print(menu[1])
    elif option == 2:
        print(menu[2])
    elif option == 3:
        print(menu[3])
    elif option == 4:
        print(menu[4])
    elif option == 0:
        quit

        

