"""
class PlayGame with attr of two names, how many points to win, dice size.
"""

from utils.player import Player
from utils.dice import Dice


class PlayGame:

    def __init__(self, player1, player2, goal, dice_size):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.goal = goal
        self.dice_size = dice_size
        self.dice = Dice(dice_size)

    def play(self):

        while (self.player1.score < self.goal and self.player2.score < self.goal):
            player1_dice_roll = self.dice.roll_dice()
            player2_dice_roll = self.dice.roll_dice()

            if(player1_dice_roll > player2_dice_roll):
                self.player1.add_points(player1_dice_roll)
                if(player1_dice_roll == self.dice_size):
                    self.player2.lose_points(player2_dice_roll)
            elif(player1_dice_roll < player2_dice_roll):
                self.player2.add_points(player2_dice_roll)
                if(player2_dice_roll == self.dice_size):
                    self.player1.lose_points(player1_dice_roll)

        if(self.player1.score > self.player2.score):
            print(
                f'The winner is {self.player1.name} with final score {self.player1.score} ')
        elif(self.player1.score < self.player2.score):
            print(
                f'The winner is {self.player2.name} with final score {self.player2.score} ')
        else:
            print(f'The game tied with score {self.goal} ')
