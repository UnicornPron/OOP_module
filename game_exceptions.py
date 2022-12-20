""" This module is for custom exceptions."""

from datetime import datetime as dt


class GameOver(Exception):
    """
    This class contains methods that are called
     when the game is over.
    """

    def __init__(self, player):
        self.player = player
        self.print_game_result()
        self.save_game_result()

    def print_game_result(self):
        """
        This method shows the result of the game.
        """
        print(f"\nPLAYER --> {self.player.name}\n"
              f"SCORE  --> {self.player.score}\n"
              f"MODE   --> {self.player.mode}")

    def save_game_result(self):
        """
        This method is for adding the result of the game to a file.
        """
        now = dt.today()
        result = ["1. ",
                  self.player.name,
                  f"{now:%d-%m-%Y}",
                  f"{now:%H:%M:%S}",
                  str(self.player.score),
                  self.player.mode]
        with open("scores.txt", "a+", encoding="utf-8") as file:
            file.write("|".join(result) + '\n')
            file.seek(0)
            result = sorted([line.split("|")[1:] for line in file],
                            key=lambda x: int(x[3]), reverse=True)

        with open("scores.txt", "w", encoding="utf-8") as file:
            for position, player in enumerate(result, 1):
                if position < 11:
                    file.write(f"{position}. |" + '|'.join(player))


class EnemyDown(Exception):
    """
    This is exception when enemy has no longer any life points.
    """


class InvalidInput(Exception):
    """
    This is the exception for user`s incorrect data input
    """
