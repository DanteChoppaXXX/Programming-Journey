#!../bin/python3

#Start with some design that needs to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Simulate printing each design, until none are left.
#Move each design tto completed_models after printing.
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        #Simulate creating a 3D print from the design.
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    #Display all completed models
    print("\nThe following models have been printed:")
    for i, completed_model in enumerate(completed_models, start=1):
        print(f'{i}. {completed_model}')

print(unprinted_designs[:])
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)