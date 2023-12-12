#!../bin/python3

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print("Enter a name: (blank to quit)")
    name = input()
    name = name.capitalize()
    if name == '':
        break
    if name in birthdays:
        print(f"{birthdays[name]} is the birthday of {name}")
    else:
        print(f"I don't have birthday information for {name}")
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated.")
