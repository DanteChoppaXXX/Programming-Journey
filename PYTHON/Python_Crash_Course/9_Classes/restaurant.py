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
print(f"{restaurant.name.title()}")
print(f"{restaurant.type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()


