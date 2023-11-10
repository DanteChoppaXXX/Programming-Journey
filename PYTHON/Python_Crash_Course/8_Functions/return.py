#!../bin/python3



# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted."""
#     full_name = f'{first_name} {middle_name} {last_name}'
#     return full_name.title()

# musician = get_formatted_name('jimmy', 'joe', 'jammy')
# musician1 = get_formatted_name('jimmy', 'jammy')
# print(musician)
# print(musician1)

# #RETURNING A DICTIONARY
# def build_person(first_name, last_name, age=None):
#     """Return a dictionary of information about a person."""
#     person = {'first':first_name.title(), 'last':last_name.title()}
#     if age:
#         person['age'] = age
#     return person

# actor = build_person('jackie', 'chan', age=65)
# print(actor)

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    message = 'PLEASE ENTER YOUR NAME'
    msg_len = len(message)
    print(message)
    print('(Enter "q" to quit!)')
    print(msg_len * '=')
    f_name = input('First name: ')
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        break
    import time
    formatted_name = get_formatted_name(f_name, l_name)
    time.sleep(1)
    print(f'\nWelcome to my world Mr. {formatted_name}\n')