#!../bin/python3

cars = ['benz', 'bugatti', 'audi', 'lexus', 'lambo', 'rarri']

cars[-1] = 'maseratti'
cars.append('ram')
cars.append('thundra')
cars.append('keke')
cars.insert(3, 'mistubishi')
cars.insert(4, 'toyota')
cars.append('rarri')
cars.insert(2, 'jeep')

popped_cars = cars.pop(-2)

del cars[-1]

for car in cars:
    print('I am buying a luxurious ' + car + ' very soon.')

print(cars)
print('I just bought a '+ popped_cars + ' last week')
print(popped_cars)