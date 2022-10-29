import unittest
from src.pgn_parser import get_only_games
from src.pgn_parser import no_long_games
from src.pgn_parser import get_winner

# TODO: Test check_path_format
# TODO: Test check_path_filename
# TODO: Test no_side_lines
# TODO: Test no_kibitz

only_games_test_list = [
    "['Opera House Test']",
    "['Paul Morphy']",
    "1. e4 e5",
    "['WmWw']",
    "['Paul Morphy']",
    "1. e4 e5"
]

long_games_test_list = [
    "1. e4 e5, 2. Nf3 d6 41. d4",
    "1. e4 e5 2. Nf3 d6 12. d4",
    "1. e4 e5, 2. Nf3 d6 112. d4"
]

winner_test_list = [
    "1. e4 e5, 2. Nf3 d6 31. d4# 1/2-1/2",
    "1. e4 e5 2. Nf3 d6 12. d4 1-0",
    "1. e4 e5 2. Nf3 d6 12. d4  Bg4 1-0",
    "1. e4 e5 2. Nf3 d6 12. d4# 1-0",
    "1. e4 e5 2. Nf3 d6 12. d4 0-1",
    "1. e4 e5 2. Nf3 d6 12. d4  Bg4 0-1",
    "1. e4 e5 2. Nf3 d6 12. d4 Bg4# 0-1",
    "1. e4 e5, 2. Nf3 d6 2. d4"
]


class TestGamesList(unittest.TestCase):
    def test_get_only_games(self):
        """Test if only the game string is return and not the bracketed meta-data"""
        test_only_games = get_only_games(only_games_test_list)
        self.assertEqual(test_only_games, ["1. e4 e5", "1. e4 e5"])

    def test_no_long_games(self):
        """Test to ensure no games over 39 moves"""
        test_no_long_games = no_long_games(long_games_test_list)
        self.assertEqual(test_no_long_games, ["1. e4 e5 2. Nf3 d6 12. d4"])

    # def test_get_winner_ww(self):
    #     """Test to see if only games ending in ( 1-0) are returned"""
    #     white_wins = get_winner(winner_test_list, 'white', False)
    #     self.assertEqual(white_wins, ["1. e4 e5 2. Nf3 d6 12. d4 1-0", "1. e4 e5 2. Nf3 d6 12. d4  Bg4 1-0",
    #                                   "1. e4 e5 2. Nf3 d6 12. d4# 1-0"])

    # def test_get_winner_wm(self):
    #     """Test to see if only games ending in (# 1-0) are returned"""
    #     white_mates = get_winner(winner_test_list, 'white', True)
    #     self.assertEqual(white_mates, ["1. e4 e5 2. Nf3 d6 12. d4# 1-0"])


if __name__ == '__main__':
    unittest.main()
