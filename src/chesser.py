"""
chesser.py pgn chess parser class file
"""
import re
import sys


class PgnParser:
    def __init__(self, pgn_file: str, max_move: str, white: bool, mate: bool):
        self.pgn_file = pgn_file
        self.max_move = max_move
        self.white = white
        self.mate = mate
        self.pgn_games = list()
        self.white_wins = list()
        self.white_mates = list()
        self.black_wins = list()
        self.black_mates = list()

        self.checker = {
            "paren_o": "(",
            "paren_c": ")",
            "brace_o": "{",
            "brace_c": "}",
            "bracket_o": "[",
            "bracket_c": "]",
            "tag_o": "<",
            "tag_c": ">",
            "white_win": " 0-1",
            "black_win": " 0-1",
            "min_move": " 10. ",
            "mate": "#",
            "start": "1. ",
            "dash": "-",
            "max_move": self.max_move,
        }

        self.first_move = re.compile("1\.\s[a-hN][1-8acfh]3?\s[a-hN][5-6acfh]6?\s2\.\s")

    def parse_file(self):
        try:
            with open(self.pgn_file, "r") as fo:
                pgn_lines = fo.readlines()
        except FileNotFoundError as fnfe:
            print(f"{fnfe}")
        else:
            for line in pgn_lines:
                if (
                    not line.startswith(self.checker["start"])
                    or not line[-3] == self.checker["dash"]
                    or self.checker["paren_o"] in line
                    or self.checker["paren_c"] in line
                    or self.checker["brace_o"] in line
                    or self.checker["brace_c"] in line
                    or self.checker["bracket_o"] in line
                    or self.checker["bracket_c"] in line
                    or self.checker["tag_o"] in line
                    or self.checker["tag_c"] in line
                    or self.checker["min_move"] not in line
                    or self.checker["max_move"] in line
                ):
                    continue
                else:
                    self.pgn_games.append(line)
        finally:
            if not self.pgn_games:
                sys.exit()

    def get_white_wins(self):
        if self.white and self.mate:
            for game in self.pgn_games:
                if game.endswith("# 1-0"):
                    if re.search(self.first_move, game):
                        self.white_mates.append(game)
        elif self.white and not self.mate:
            for game in self.pgn_games:
                if game.endswith(" 1-0") and "#" not in game:
                    if re.search(self.first_move, game):
                        self.white_wins.append(game)

    def get_black_wins(self):
        if not self.white and self.mate:
            for game in self.pgn_games:
                if game.endswith("# 0-1"):
                    if re.search(self.first_move, game):
                        self.black_mates.append(game)
        elif not self.white and not self.mate:
            for game in self.pgn_games:
                if game.endswith(" 0-1") and "#" not in game:
                    if re.search(self.first_move, game):
                        self.black_wins.append(game)


def main():
    pass

if __name__ == "__main__":
    main()
