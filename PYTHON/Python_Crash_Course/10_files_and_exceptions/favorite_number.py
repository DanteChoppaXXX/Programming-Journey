#!../bin/python3
import json

filename = 'fav_num.json'

def get_fav_num():
    #Prompt the user for their favorite number
    fav_num = input("What's your favorite number?: ")

    #Store the number in a file with json.dump()
    with open(filename, 'w') as fav:
        json.dump(fav_num, fav)

#Read the value from the saved file 
def read_file():
    with open(filename) as file:
        content = json.load(file)
        return content

#Display the message "I know your favorite number!, It's ____"
def msg():
    try:
        guess = "I know your favorite number!, It's " + read_file()
        print(guess)
    except FileNotFoundError:
        get_fav_num()
        
msg()