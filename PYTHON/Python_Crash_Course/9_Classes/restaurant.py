#!../bin/python3

class Restaurant():
    """Modeling a restaurant"""

    def __init__(self, restaurant_name, restaurant_type):
        self.name = restaurant_name
        self.type = restaurant_type
        self.number_served = 1500

    def describe_restaurant(self):
        print(f"Name: {self.name}")
        print(f"Type: {self.type}")

    def open_restaurant(self):
        print(f"{self.name} is opened")

    def increment_number_served(self, serve):
        print(f"Customer Served Today: {serve}")

    def set_number_served(self, served):
        self.number_served = served
        print(f"Total Customer Served: {self.number_served}")

class IceCreamStand(Restaurant):
    """Modeling a child class for the Restaurant class."""
    def __init__(self, restaurant_name, restaurant_type, flavors):
        super().__init__(restaurant_name, restaurant_type)
        """Create a list of ice cream flavors"""
        flavors = ['vanilla', 'strawberry', 'banana', 'chocolate']
        self.flavors = flavors

    def flavors_list(self):
        """Display the list of available flavors to the customer."""
        print(self.flavors)

iceCreamStand0 = IceCreamStand('Raheti', 'Eatery', 'flavors' )
iceCreamStand0.flavors_list()


# restaurant = Restaurant("Oasis", "Eatery")
# restaurant0 = Restaurant("Sandton Gold", "Hotel")
# restaurant1 = Restaurant("Dalco", "Guest House")

# #print(f"{restaurant.name.title()}")
# #print(f"{restaurant.type}")

# restaurant.describe_restaurant()
# restaurant.set_number_served(800)
# restaurant.open_restaurant()
# print('___________________')
# restaurant0.describe_restaurant()
# restaurant0.set_number_served(1500)
# print('___________________')
# restaurant1.describe_restaurant()
# restaurant1.set_number_served(200)
# restaurant1.increment_number_served(2)

#print(f"Customer Served: {restaurant1.number_served}")
