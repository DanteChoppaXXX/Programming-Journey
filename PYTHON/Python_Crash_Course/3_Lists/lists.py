#!../bin/python3
cars = ['benz', 'bugatti', 'audi', 'lexus', 'lambo', 'rarri']

#cars.remove('audi')
#print(cars)

too_expensive = 'audi'
cars.remove(too_expensive)
print(cars)
print("\nAn " + too_expensive + ' is too expensive right now, go for the ' + cars[1] + ' instead.')
