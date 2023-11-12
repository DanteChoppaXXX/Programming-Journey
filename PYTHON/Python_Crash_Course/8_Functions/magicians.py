#!../bin/python3

#list of magician's names.
magicians = ['mike', 'jimmy', 'joe', 'zack']
great_magicians = []

def show_magicians(magicians):
    """Print the names of the magicians."""
    for i, magician in enumerate(magicians, start=1):
        print(f'{i}. {magician}')

def make_great(magicians, great_magicians):
    """Modify the list of magicians to title them great magicians."""
    while magicians:
        become_great = 'The Great '
        become_great += magicians.pop()
        great_magicians.append(become_great)

show_magicians(magicians)
make_great(magicians[:], great_magicians)
print(magicians)
print(great_magicians)
print('\n\nTHE GREAT AND MIGHTY DRAGON')