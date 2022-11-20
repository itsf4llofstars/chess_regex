"""
NOTE: In order to run your own tests you will need to change
the self.assertEqual(test_directory, 'CHANGE_THIS_PATH')
line to a valid directory on your computer
"""
import unittest
from src.menu import check_dir
from src.menu import check_file_exists


class TestMenu(unittest.TestCase):
    def test_check_dir(self):
        test_directory = check_dir('chess_games_dir')
        self.assertEqual(test_directory, '/home/bumper/chess_games_dir')

    def test_check_file_exists(self):
        test_file = check_file_exists('/home/bumper/python/chess_regex', 'README.md')
        self.assertEqual(test_file, '/home/bumper/python/chess_regex/README.md')
