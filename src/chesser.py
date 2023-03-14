"""
chesser.py pgn chess parser class file
"""


class PgnParser:
    def __init__(self, pgn_file: str, max_move: str, white: bool, mate: bool):
        self.pgn_file = pgn_file
        self.max_move = max_move
        self.white = white
        self.mate = mate
        self.pgn_games = []

        checker = {
                'paren_o': '(', 'paren_c': ')',
                'brace_o': '{', 'brace_c': '}',
                'bracket_o': '[', 'bracket_c': ']',
                'tag_o': '<', 'tag_c': '>',
                'white_win': ' 0-1', 'black_win': ' 0-1',
                'min_move': ' 10. ', 'mate': '#',
                'start': '1. ', 'dash': '-', 'max_move': self.max_move,
                }

        def parse_file(self):
            try:
                with open(self.pgn_file, 'r') as fo:
                    pgn_lines = fo.readlines()
            except FileNotFoundError as fnfe:
                print(f"{fnfe}")
            else:
                for line in pgn_lines:
                    if (
                        line.startswith(checker['start'])
                        and line[-3] == checker['dash']
                        and checker['paren_o'] not in line
                        and checker['paren_c'] not in line
                        and checker['brace_o'] not in line
                        and checker['brace_c'] not in line
                        and checker['bracket_o'] not in line
                        and checker['bracket_c'] not in line
                        and checker['tag_o'] not in line
                        and checker['tag_c'] not in line
                        and checker['min_move'] in line
                        and checker['max_move'] not in line
                    ):
                        self.pgn_games.append(line)
                        # continue making it smaller
