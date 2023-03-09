import unittest

from src.big_parser import parse_games


class TestBigParser(unittest.TestCase):
    def test_parse_games_ww(self):
        """Test if the game returned is won by white"""
        test_white_won = parse_games(test_games_list, ' 30. ', ' 10. ', True, False)
        self.assertEqual(test_white_won,
                         '1. e4 e5 2. Nf3 d6 3. d4 Bf4 4. dxe5 1-0'
        )