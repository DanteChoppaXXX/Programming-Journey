#!../bin/python3

# filename = 'programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write('I love Programming.\n')

guest_list = 'guest_list.txt'
code = 'programming.txt'

# keep_going = True

# while(keep_going):
#     user = input("What's your name?: ")
#     message = 'Hello ' + user.title()
#     print(message)
#     question = input("Why do you like programming?: ")
#     answer = question
    
#     with open(guest_list, 'a') as f:
#         f.write(f"{user.title()}: {answer}\n")
#         # f.write(f"{answer}\n")
#     print(answer.split())
#     
def count_words(filename):    
    try:
        with open(filename) as file:
            words = file.read()
            num_words = words.split()
            print(f"The file {filename} has {len(num_words)} words.")
    except FileNotFoundError:
        msg = 'Sorry ' + filename + ' does not exist.\n'
        with open('missing_file.txt', 'a') as mf:
            mf.write(msg)
        # print(msg)
        #pass

keep_going = False

filenames = [guest_list, code, 'files.txt', 'list.txt']
for filename in filenames:
    count_words(filename)