"""
class Dice can initialize dice with an arbitrary number of sides. 1 to n inclusive
of n
"""

import random


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self):
        return (random.randint(1, self.sides))
