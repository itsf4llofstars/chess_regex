"""
chesser.py pgn chess parser class file
"""
import sys


class PgnParser:
    def __init__(self, pgn_file: str, max_move: str, white: bool, mate: bool):
        self.pgn_file = pgn_file
        self.max_move = max_move
        self.white = white
        self.mate = mate
        self.pgn_games = []

        checker = {
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

        def parse_file(self):
            try:
                with open(self.pgn_file, "r") as fo:
                    pgn_lines = fo.readlines()
            except FileNotFoundError as fnfe:
                print(f"{fnfe}")
            else:
                for line in pgn_lines:
                    if (
                        not line.startswith(checker["start"])
                        or not line[-3] == checker["dash"]
                        or checker["paren_o"] in line
                        or checker["paren_c"] in line
                        or checker["brace_o"] in line
                        or checker["brace_c"] in line
                        or checker["bracket_o"] in line
                        or checker["bracket_c"] in line
                        or checker["tag_o"] in line
                        or checker["tag_c"] in line
                        or checker["min_move"] not in line
                        or checker["max_move"] in line
                    ):
                        continue
                    else:
                        self.pgn_games.append(line)
            finally:
                if not self.pgn_games:
                    sys.exit()
