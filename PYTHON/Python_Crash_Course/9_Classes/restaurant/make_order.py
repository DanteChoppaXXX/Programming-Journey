#!../../bin/python3
from restaurant import Restaurant
from icecream_stand import IceCreamStand

iceCreamStand0 = IceCreamStand('Raheti', 'Eatery', 'flavors' )
iceCreamStand0.flavors_list()


# restaurant = Restaurant("Oasis", "Eatery")
# restaurant0 = Restaurant("Sandton Gold", "Hotel")
restaurant1 = Restaurant("Dalco", "Guest House")

# #print(f"{restaurant.name.title()}")
# #print(f"{restaurant.type}")

# restaurant.describe_restaurant()
# restaurant.set_number_served(800)
# restaurant.open_restaurant()
# print('___________________')
# restaurant0.describe_restaurant()
# restaurant0.set_number_served(1500)
# print('___________________')
restaurant1.describe_restaurant()
restaurant1.set_number_served(200)
restaurant1.increment_number_served(2)

print(f"Customer Served: {restaurant1.number_served}")