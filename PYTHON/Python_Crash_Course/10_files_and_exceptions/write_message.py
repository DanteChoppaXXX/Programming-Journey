#!../bin/python3

# filename = 'programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write('I love Programming.\n')

guest_list = 'guest_list.txt'

keep_going = True

while(keep_going):
    user = input("What's your name?: ")
    message = 'Hello ' + user.title()
    print(message)
    question = input("Why do you like programming?: ")
    answer = question
    with open(guest_list, 'a') as f:
        f.write(f"{user.title()}: {answer}\n")
        # f.write(f"{answer}\n")
    print(answer.split())
    with open(guest_list) as file:
        words = file.read()
        num_words = words.split()
        print(len(num_words))
    keep_going = False