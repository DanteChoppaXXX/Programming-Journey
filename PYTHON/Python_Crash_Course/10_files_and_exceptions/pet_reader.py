#!../bin/python3

#pet_files = ['cat.txt', 'dog.txt']

file = 'missing_file.txt'
with open(file) as f:
    content = f.read()
    #count = content.count('sorry')
    count = content.lower().count('sorry')
    print(count)
    