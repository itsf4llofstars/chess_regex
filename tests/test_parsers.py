import unittest

# TODO: Add documentaton

from src.pgn_parsers import get_black_mates
from src.pgn_parsers import get_black_wins
from src.pgn_parsers import get_only_games
from src.pgn_parsers import get_white_mates
from src.pgn_parsers import get_white_wins
from src.pgn_parsers import no_long_games
from src.pgn_parsers import set_max_move
from src.pgn_parsers import omit_kibitz_games
from src.pgn_parsers import replace_tags
from src.pgn_parsers import strip_black_mates
from src.pgn_parsers import strip_white_mates
from src.pgn_parsers import pick_one_game
from src.pgn_parsers import regex_dict

only_games_test_list = [
        "['Paul Morphy']",
        "1. e4 e5 2. Nf3 d6 3. d4 Bf4 4. dxe5 Bxf3 1-0",
        "['Opera House Test']",
        "1. e4 e5 2. Nf3 d6 3. d4 Bf4 4. dxe5 Bxf3 0-1",
        ]

# We can change the last move number and change the
# set_max_moves argument in the test_no_long_games
# test method. To return the 49. moves game set_max_moves
# argument should be 5, the previous games should have
# moves greater than 49. You will also have to change
# the assertEqual pass string
long_games_test_list = [
        "1. e4 e5 2. Nf3 d6 39. d4",
        "1. e4 e5 2. Nf3 d6 43. d4",
        "1. e4 e5 2. Nf3 d6 55. d4",
        ]

winner_test_list = [
        "1. e4 e5 2. Nf3 d6 12. d4 1-0",
        "1. e4 e5 2. Nf3 d6 12. d4 Bg4 1-0",
        "1. e4 e5 2. Nf3 d6 12. d4 Bg4 0-1",
        "1. e4 e5 2. Nf3 d6 12. d4 Bg4# 0-1",
        "1. e4 e5 2. Nf3 d6 12. d4# 1-0",
        "1. e4 e5 2. Nf3 d6 12. d4 0-1",
        "1. e4 e5, 2. Nf3 d6 2. d4",
        "1. e4 e5, 2. Nf3 d6 31. d4# 1/2-1/2",
        ]

winner_test_list1 = ["1. c4 e5 2. Nf3 d6 12. d4 1-0", "1. e4 e5 2. Nf3 d6 2. d4 0-1"]

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
        "1. e4 e5 2. Nf3 d6 31. d4# 1/2-1/2",
        ]

kibitz_games_list = [
        "1. c4 e5 2. Nf3 d6 12. d4 1-0",
        "1. e4 e5 { This is kibitz } 2. Nf3 d6 2. d4 0-1",
        "1. c4 d5 2. Nf3 d6 12. d4 1-0",
        "1. e4 e5 2. Nf3 ( 2. Nc3 g6 ) 2... d6 2. d4 0-1",
        ]

tagged_games_list = [
        "1. c4 d5! 2. Nf3!! d6? 12. d4?? d4?! 12. d4!? d4+- 12. d4-+ d4+ 1-0"
        ]

one_game_list = [
        "1. c4 e5 2. Nf3 d6 12. d4 1-0",
        "1. c4 e5 2. Nf3 d6 12. d4 1-0",
        ]

# NOTE: These test are not exhaustive


class TestGamesList(unittest.TestCase):
    def test_get_only_games(self):
        """Test if only the game string is return and not the bracketed meta-data"""
        test_only_games = get_only_games(only_games_test_list)
        self.assertEqual(
                test_only_games,
                [
                    "1. e4 e5 2. Nf3 d6 3. d4 Bf4 4. dxe5 Bxf3 1-0",
                    "1. e4 e5 2. Nf3 d6 3. d4 Bf4 4. dxe5 Bxf3 0-1",
                    ],
                )

    def test_no_long_games(self):
        """Test to ensure no games over 39 moves"""
        set_max_move(5)
        test_no_long_games = no_long_games(long_games_test_list)
        self.assertEqual(
                test_no_long_games,
                [
                    "1. e4 e5 2. Nf3 d6 39. d4",
                    "1. e4 e5 2. Nf3 d6 43. d4",
                    ],
                )

    def test_get_white_wins(self):
        """Test that get_wite_wins list is populated with wins by white"""
        test_white_wins = []
        get_white_wins(winner_test_list, test_white_wins)
        self.assertEqual(
                test_white_wins,
                [
                    "1. e4 e5 2. Nf3 d6 12. d4 1-0",
                    "1. e4 e5 2. Nf3 d6 12. d4 Bg4 1-0",
                    "1. e4 e5 2. Nf3 d6 12. d4# 1-0",
                    ],
                )

    def test_get_white_mates(self):
        """Test get_white_mates list is populated with white checkmates"""
        test_white_mates = []
        get_white_mates(winner_test_list, test_white_mates)
        self.assertEqual(test_white_mates, ["1. e4 e5 2. Nf3 d6 12. d4# 1-0"])

    def test_get_black_wins(self):
        """Test get_black_wins list is populated with wins by black"""
        test_black_wins = []
        get_black_wins(winner_test_list, test_black_wins)
        self.assertEqual(
                test_black_wins,
                [
                    "1. e4 e5 2. Nf3 d6 12. d4 Bg4 0-1",
                    "1. e4 e5 2. Nf3 d6 12. d4 Bg4# 0-1",
                    "1. e4 e5 2. Nf3 d6 12. d4 0-1",
                    ],
                )

    def test_get_black_mates(self):
        """Test get_black_mates list is populated with black checkmates"""
        test_black_mates = []
        get_black_mates(winner_test_list, test_black_mates)
        self.assertEqual(test_black_mates, ["1. e4 e5 2. Nf3 d6 12. d4 Bg4# 0-1"])

    def test_strip_white_mates(self):
        """Test that the last white move is stripped off"""
        test_strip_white_mates = []
        strip_white_mates(strip_mates_test_list, test_strip_white_mates)
        self.assertEqual(
                test_strip_white_mates,
                [
                    "1. e4 e5 2. Nf3 d6",
                    "1. e4 e5 2. Nf3 d6",
                    "1. e4 e5 2. Nf3 d6",
                    ],
                )

    def test_strip_black_mates(self):
        """Test that the last black move is stripped off"""
        test_strip_black_mates = []
        strip_black_mates(strip_mates_test_list, test_strip_black_mates)
        self.assertEqual(
                test_strip_black_mates,
                [
                    "1. e4 e5 2. Nf3 d6 12. d4",
                    "1. e4 e5 2. Nf3 d6 22. d4",
                    "1. e4 e5 2. Nf3 d6 32. d4",
                    ],
                )

    def test_omit_kibitz_games(self):
        """Test that there are no kibitzing symbols in the games"""
        test_omit_kibitz = omit_kibitz_games(kibitz_games_list)
        self.assertEqual(
                test_omit_kibitz,
                ["1. c4 e5 2. Nf3 d6 12. d4 1-0", "1. c4 d5 2. Nf3 d6 12. d4 1-0"],
                )

    def test_replace_tags(self):
        """Test that all annotation tags are removed"""
        test_no_tagged = replace_tags(tagged_games_list)
        self.assertEqual(
                test_no_tagged, ["1. c4 d5 2. Nf3 d6 12. d4 d4 12. d4 d4 12. d4 d4 1-0"]
                )

    def test_pick_one_game(self):
        """Test that the pick_one_game func picks one game only"""
        test_one_game = pick_one_game(one_game_list)
        self.assertEqual(
                test_one_game, ["1.", "c4", "e5", "2.", "Nf3", "d6", "12.", "d4", "1-0"]
                )

    def test_set_max_move(self):
        pass


if __name__ == "__main__":
    unittest.main()
