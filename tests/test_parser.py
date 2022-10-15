import unittest
from src.pgn_parser import get_only_games

only_games_test_list = [
    "['Opera House Test']",
    "['Paul Morphy']",
    "1. e4 e5",
    "['WmWw']",
    "['Paul Morphy']",
    "1. e4 e5"
]


class MyTestCase(unittest.TestCase):
    def test_get_only_games(self):
        """Test if only the game string is return and not the bracketed meta-data"""
        test_only_games = get_only_games(only_games_test_list)
        self.assertEqual(test_only_games, ["1. e4 e5", "1. e4 e5"])


if __name__ == '__main__':
    unittest.main()
