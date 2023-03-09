"""Thiese tests are not exhaustive."""
import unittest

from src.big_parser import parse_games

class TestBigParser(unittest.TestCase):
    def test_parse_games_ww(self):
        """Test if the game returned is won by white"""
        test_white_won = parse_games('./tests/big_parser_test.pgn', ' 30. ', ' 3. ', True, False)
        self.assertEqual(test_white_won,
                         '1. e4 e5 2. Nf3 d6 3. d4 Bf4 4. dxe5 1-0'
        )
    
    def test_parse_games_wm(self):
        """Test if the game returned is a mate by white"""
        test_white_won = parse_games('./tests/big_parser_test.pgn', ' 30. ', ' 3. ', True, True)
        self.assertEqual(test_white_won,
                         '1. e4 e5 2. Nf3 d6 3. d4 Bf4 4. dxe5# 1-0'
        )

    def test_parse_games_bw(self):
        """Test if the game returned is won by black"""
        test_white_won = parse_games('./tests/big_parser_test.pgn', ' 30. ', ' 3. ', False, False)
        self.assertEqual(test_white_won,
                         '1. e4 e5 2. Nf3 d6 3. d4 Bf4 4. dxe5 Bxf3 0-1'
        )

    def test_parse_games_bm(self):
        """Test if the game returned is a mate by black"""
        test_white_won = parse_games('./tests/big_parser_test.pgn', ' 30. ', ' 3. ', False, True)
        self.assertEqual(test_white_won,
                         '1. e4 e5 2. Nf3 d6 3. d4 Bf4 4. dxe5 Bxf3# 0-1'
        )