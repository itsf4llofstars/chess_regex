import unittest
from src.pgn_parsers import get_only_games
from src.pgn_parsers import no_long_games
from src.pgn_parsers import get_white_wins

only_games_test_list = [
    "['Opera House Test']",
    "['Paul Morphy']",
    "1. e4 e5 2. Nf3 d6 3. d4 Bf4 4. dxe5 Bxf3 1-0",
    "['Opera House Test']",
    "['Paul Morphy']",
    "1. e4 e5 2. Nf3 d6 3. d4 Bf4 4. dxe5 Bxf3 0-1"
]

long_games_test_list = [
    "1. Nc3 e5, 2. Nf3 d6 41. d4",
    "1. e4 e5 2. Nf3 d6 12. d4",
    "1. e4 Nf6, 123. Nf3 d6 25. d4"
]

winner_test_list = [
    "1. e4 e5 2. Nf3 d6 12. d4 1-0",
    "1. e4 e5 2. Nf3 d6 12. d4  Bg4 1-0",
    "1. e4 e5 2. Nf3 d6 12. d4# 1-0",
    "1. e4 e5 2. Nf3 d6 12. d4 0-1",
    "1. e4 e5 2. Nf3 d6 12. d4  Bg4 0-1",
    "1. e4 e5 2. Nf3 d6 12. d4 Bg4# 0-1",
    "1. e4 e5, 2. Nf3 d6 2. d4"
    "1. e4 e5, 2. Nf3 d6 31. d4# 1/2-1/2",
]

winner_test_list1 = [
    "1. c4 e5 2. Nf3 d6 12. d4 1-0",
    "1. e4 e5, 2. Nf3 d6 2. d4 0-1"
]


class TestGamesList(unittest.TestCase):
    def test_get_only_games(self):
        """Test if only the game string is return and not the bracketed meta-data"""
        test_only_games = get_only_games(only_games_test_list)
        self.assertEqual(test_only_games, ["1. e4 e5 2. Nf3 d6 3. d4 Bf4 4. dxe5 Bxf3 1-0", "1. e4 e5 2. Nf3 d6 3. d4 Bf4 4. dxe5 Bxf3 0-1"])

    def test_no_long_games(self):
        """Test to ensure no games over 39 moves"""
        test_no_long_games = no_long_games(long_games_test_list)
        self.assertEqual(test_no_long_games, ["1. e4 e5 2. Nf3 d6 12. d4"])

    def test_get_white_wins(self):
        test_winner = []
        get_white_wins(winner_test_list, test_winner)
        self.assertEqual(test_winner, [
            "1. e4 e5 2. Nf3 d6 12. d4 1-0",
            "1. e4 e5 2. Nf3 d6 12. d4  Bg4 1-0",
            "1. e4 e5 2. Nf3 d6 12. d4# 1-0"
        ])
                                     

    def test_get_winner_wm(self):
        """Test to see if only games ending in (# 1-0) are returned"""
        white_mates = get_winner(winner_test_list, 'white', True)
        self.assertEqual(white_mates, ["1. e4 e5 2. Nf3 d6 12. d4# 1-0"])


if __name__ == '__main__':
    unittest.main()
