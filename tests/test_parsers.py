import unittest

from src.pgn_parsers import get_black_mates
from src.pgn_parsers import get_black_wins
from src.pgn_parsers import get_only_games
from src.pgn_parsers import get_white_mates
from src.pgn_parsers import get_white_wins
from src.pgn_parsers import no_long_games
from src.pgn_parsers import ommit_kibitz_games
from src.pgn_parsers import replace_tags
from src.pgn_parsers import strip_black_mates
from src.pgn_parsers import strip_white_mates

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
    "1. e4 e5 2. Nf3 d6 12. d4 Bg4 1-0",
    "1. e4 e5 2. Nf3 d6 12. d4# 1-0",
    "1. e4 e5 2. Nf3 d6 12. d4 0-1",
    "1. e4 e5 2. Nf3 d6 12. d4 Bg4 0-1",
    "1. e4 e5 2. Nf3 d6 12. d4 Bg4# 0-1",
    "1. e4 e5, 2. Nf3 d6 2. d4",
    "1. e4 e5, 2. Nf3 d6 31. d4# 1/2-1/2"
]

winner_test_list1 = [
    "1. c4 e5 2. Nf3 d6 12. d4 1-0",
    "1. e4 e5 2. Nf3 d6 2. d4 0-1"
]

strip_mates_test_list = [
    "1. e4 e5 2. Nf3 d6 12. d4 1-0",
    "1. e4 e5 2. Nf3 d6 12. cxd8=Q 1-0",
    "1. e4 e5 2. Nf3 d6 12. d4# 1-0",
    "1. e4 e5 2. Nf3 d6 12. Nxd4# 1-0",
    "1. e4 e5 2. Nf3 d6 12. fxd8=B# 1-0",
    "1. e4 e5 2. Nf3 d6 12. d4 Bg4# 0-1",
    "1. e4 e5 2. Nf3 d6 12. d4 Bg4 0-1",
    "1. e4 e5 2. Nf3 d6 22. d4 f8=R# 0-1",
    "1. e4 e5 2. Nf3 d6 32. d4 N3g5# 0-1",
    "1. e4 e5 2. Nf3 d6 31. d4# 1/2-1/2"
]

kibitz_games_list = [
    "1. c4 e5 2. Nf3 d6 12. d4 1-0",
    "1. e4 e5 { This is kibitz } 2. Nf3 d6 2. d4 0-1",
    "1. c4 d5 2. Nf3 d6 12. d4 1-0",
    "1. e4 e5 2. Nf3 ( 2. Nc3 g6 ) 2... d6 2. d4 0-1"
]

tagged_games_list = [
    "1. c4 d5! 2. Nf3!! d6? 12. d4?? d4?! 12. d4!? d4+- 12. d4-+ d4+ 1-0",
    "1. c4 d5 2. Nf3 d6 12. d4 d4 12. d4 d4 12. d4 d4 1-0"
]


# NOTE: These test are not exhaustive


class TestGamesList(unittest.TestCase):
    def test_get_only_games(self):
        """Test if only the game string is return and not the bracketed meta-data"""
        test_only_games = get_only_games(only_games_test_list)
        self.assertEqual(test_only_games, [
            "1. e4 e5 2. Nf3 d6 3. d4 Bf4 4. dxe5 Bxf3 1-0",
            "1. e4 e5 2. Nf3 d6 3. d4 Bf4 4. dxe5 Bxf3 0-1"
        ])

    def test_no_long_games(self):
        """Test to ensure no games over 39 moves"""
        test_no_long_games = no_long_games(long_games_test_list)
        self.assertEqual(test_no_long_games, ["1. e4 e5 2. Nf3 d6 12. d4"])

    def test_get_white_wins(self):
        test_white_wins = []
        get_white_wins(winner_test_list, test_white_wins)
        self.assertEqual(test_white_wins, [
            "1. e4 e5 2. Nf3 d6 12. d4 1-0",
            "1. e4 e5 2. Nf3 d6 12. d4 Bg4 1-0",
            "1. e4 e5 2. Nf3 d6 12. d4# 1-0"
        ])

    def test_get_white_mates(self):
        test_white_mates = []
        get_white_mates(winner_test_list, test_white_mates)
        self.assertEqual(test_white_mates, ["1. e4 e5 2. Nf3 d6 12. d4# 1-0"])

    def test_get_black_wins(self):
        test_black_wins = []
        get_black_wins(winner_test_list, test_black_wins)
        self.assertEqual(test_black_wins, [
            "1. e4 e5 2. Nf3 d6 12. d4 0-1",
            "1. e4 e5 2. Nf3 d6 12. d4 Bg4 0-1",
            "1. e4 e5 2. Nf3 d6 12. d4 Bg4# 0-1"
        ])

    def test_get_black_mates(self):
        test_black_mates = []
        get_black_mates(winner_test_list, test_black_mates)
        self.assertEqual(test_black_mates, ["1. e4 e5 2. Nf3 d6 12. d4 Bg4# 0-1"])

    def test_strip_white_mates(self):
        test_strip_white_mates = []
        strip_white_mates(strip_mates_test_list, test_strip_white_mates)
        self.assertEqual(test_strip_white_mates,
                         [
                             "1. e4 e5 2. Nf3 d6",
                             "1. e4 e5 2. Nf3 d6",
                             "1. e4 e5 2. Nf3 d6",
                         ])

    def test_strip_black_mates(self):
        test_strip_black_mates = []
        strip_black_mates(strip_mates_test_list, test_strip_black_mates)
        self.assertEqual(test_strip_black_mates,
                         [
                             "1. e4 e5 2. Nf3 d6 12. d4",
                             "1. e4 e5 2. Nf3 d6 22. d4",
                             "1. e4 e5 2. Nf3 d6 32. d4",
                         ])

    def test_ommit_kibitz_games(self):
        test_ommit_kibitz = ommit_kibitz_games(kibitz_games_list)
        self.assertEqual(test_ommit_kibitz,
                         [
                             "1. c4 e5 2. Nf3 d6 12. d4 1-0",
                             "1. c4 d5 2. Nf3 d6 12. d4 1-0"
                         ])

    def test_replace_tags(self):
        test_no_tagged = replace_tags(tagged_games_list)
        self.assertEqual(test_no_tagged,
                         [
                             "1. c4 d5 2. Nf3 d6 12. d4 d4 12. d4 d4 12. d4 d4 1-0",
                             "1. c4 d5 2. Nf3 d6 12. d4 d4 12. d4 d4 12. d4 d4 1-0"
                         ])


if __name__ == '__main__':
    unittest.main()
