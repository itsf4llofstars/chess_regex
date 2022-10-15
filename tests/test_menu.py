import unittest
from src.menu import check_dir


class TestMenu(unittest.TestCase):
    def test_check_dir(self):
        """Test if True is returned on a known
        directory
        """
        test_directory = check_dir('python/chess_regex')
        self.assertEqual(test_directory, True)

