import unittest
from src.menu import check_dir
from src.menu import check_file_exists
from src.menu import set_max_move


class TestMenu(unittest.TestCase):
    def test_check_dir(self):
        test_directory = check_dir('chess_games_dir')
        self.assertEqual(test_directory, '/home/bumper/chess_games_dir')

    def test_check_file_exists(self):
        test_file = check_file_exists('/home/bumper/python/chess_regex', 'README.md')
        self.assertEqual(test_file, '/home/bumper/python/chess_regex/README.md')

    def test_set_max_move(self):
        test_max_move = set_max_move(5)
        self.assertEqual(test_max_move, '5')
