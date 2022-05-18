"""
Main function to to call game play.
"""
from utils.play_game import PlayGame


if __name__ == "__main__":

    game = PlayGame('Joe', 'Mrtin', 25, 6)
    game.play()
