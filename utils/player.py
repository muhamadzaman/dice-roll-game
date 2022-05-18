"""
class player with attr name and initial score 0.
"""


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_points(self, points):
        self.score += points
        print(
            f'{self.name} has gained {points} points. Total score is now {self.score} points.')

    def lose_points(self, points):
        self.score -= points
        if(self.score < 0):
            self.score = 0
        print(
            f'{self.name} has lost {points} points. Total score is now {self.score} points.')
