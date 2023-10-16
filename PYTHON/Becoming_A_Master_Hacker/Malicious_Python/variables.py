#!../bin/python3

# name = 'PuppetMaster'

# print('Greetings to ' + name + ' and Welcome To This Journey To Become A Master Hacker!')

# stringvariable = 'Getting started becoming  a master hacker'
# integervariable = 23
# floatingpointvariable = 32.84
# simplelist = [0,1,2,3,4,5]
# simpledictionary = {'name':'Sasori', 'value': 43}

# #simpledictionary['name']:'Kakashi'

# print(stringvariable)
# print(integervariable)
# print(floatingpointvariable)
# print(max(simplelist))
# print(min(simplelist))
# print(hex(simplelist[3]))
# print(simpledictionary)

for password in passwords:
    Attempt = connect(username, password)

    if attempt == "230":
        print("Password found: " + password)
        sys.exit(0)
        