#!../bin/python3

def make_shirt(size='large', shirt_print='I Love Python'):
    """This function creates custom shirt description."""
    message = f"This shirt is a {size} sized shirt and it has '{shirt_print}' printed on it"
    print(message)

make_shirt()
make_shirt('medium')
make_shirt('extra large', 'Puppet Master')
#make_shirt('large', 'Devil May Cry')   #Positional Argument
#make_shirt(shirt_print='Devil May Care', size='medium')    #Keyword Argument