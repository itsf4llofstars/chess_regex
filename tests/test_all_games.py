import unittest

# from src.pgn_parsers import get_black_mates
# from src.pgn_parsers import get_black_wins
from src.pgn_parsers import get_only_games
# from src.pgn_parsers import get_white_mates
# from src.pgn_parsers import get_white_wins
# from src.pgn_parsers import no_long_games
# from src.pgn_parsers import omit_kibitz_games
# from src.pgn_parsers import replace_tags
# from src.pgn_parsers import strip_black_mates
# from src.pgn_parsers import strip_white_mates
# from src.pgn_parsers import set_max_move
# from src.pgn_parsers import regex_dict

all_games = [
    "1. e4 e5 2. Nf3! d6!! 3. d4? Bf4?? 4. dxe5+ Bxf3 1-0",
    "1. e4 Bc5 2. Nf3 d6 3. d4 Bf4 4. dxe5 Bxf3 1-0",
    ["Meta Date"],
    # "1. Nc3 e5 2. Nf3+- d6-+ 3. d4 Bf4 4. dxe5 Bxf3 0-1"
    "1. e4 Nf6 2. Nf3 d6 3. d4 Bf4 4. dxe5# 1-0"
    # "1. Nc3 Nf6 2. e4 d6 3. d4 Bf4 4. dxe5 Bxf3# 0-1"

]


class TestAllGamesList(unittest.TestCase):
    def test_get_only_games(self):
        """Test if only the game string is return and not the bracketed meta-data"""
        test_only_games = get_only_games(all_games)
        self.assertEqual(test_only_games, [
            "1. e4 e5 2. Nf3! d6!! 3. d4? Bf4?? 4. dxe5+ Bxf3 1-0",
            "1. e4 Nf6 2. Nf3 d6 3. d4 Bf4 4. dxe5# 1-0"
        ])