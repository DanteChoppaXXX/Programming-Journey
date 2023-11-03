#!../bin/python3

#Store the file path in a variable
file_path = '/home/sasori/answer.txt'

#Open and Read the file content
with open(file_path) as file_object:
    lines = file_object.readlines()

#Iterate through each lines and print out each lines without an extra newline.    
for line in lines:
        print(line.rstrip())