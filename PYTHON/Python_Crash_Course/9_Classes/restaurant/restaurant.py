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

