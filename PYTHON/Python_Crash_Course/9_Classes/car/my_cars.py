#!../bin/python3
from car import Car
from electric_car import ElectricCar

# my_bugatti = Car('bugatti', 'cheron', 2022)
my_bugatti = Car('bugatti', 'cheron', 2022)
print(my_bugatti.get_descriptive_name())

print('===================')

# my_tesla = ElectricCar('tesla', 'model X', 2023)
my_tesla = ElectricCar('tesla', 'model X', 2023)
print(my_tesla.get_descriptive_name())