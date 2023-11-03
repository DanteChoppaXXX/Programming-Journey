#!../bin/python3
from random import randint

class Die():
    """Simulating a game of dice"""
    def __init__(self, sides=20):
        self.sides = sides

    def roll_die(self):
        result = randint(1, self.sides)
        return result
    
die_roll = Die(20)
for i in range(10):
    result = die_roll.roll_die()
    print("Die roll result:", result)