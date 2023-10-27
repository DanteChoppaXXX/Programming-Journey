#!../bin/python3

class Restaurant():
    """Modeling a restaurant"""

    def __init__(self, restaurant_name, restaurant_type):
        self.name = restaurant_name
        self.type = restaurant_type

    def describe_restaurant(self):
        print(self.name)
        print(self.type)

    def open_restaurant(self):
        print(f"{self.name} is opened")

restaurant = Restaurant("Oasis", "Eatery")
restaurant0 = Restaurant("Sandton Gold", "Hotel")
restaurant1 = Restaurant("Dalco", "Guest House")

#print(f"{restaurant.name.title()}")
#print(f"{restaurant.type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()
print('___________________')
restaurant0.describe_restaurant()
print('___________________')
restaurant1.describe_restaurant()

