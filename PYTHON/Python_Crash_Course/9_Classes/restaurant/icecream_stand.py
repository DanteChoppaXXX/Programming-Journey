#!../../bin/python3
from restaurant import Restaurant

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