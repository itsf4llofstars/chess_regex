import unittest
from src.menu import check_dir
from src.menu import check_file_exists


class TestMenu(unittest.TestCase):
    def test_check_dir(self):
        """Test if True is returned on a known
        directory
        """
        test_directory = check_dir('python/chess_regex')
        self.assertEqual(test_directory, True)

    def test_check_file_exists(self):
        """Checks if True is return on the existance of
        a file
        """
        test_file = check_file_exists('python/chess_regex', 'README.md')
        self.assertEqual(test_file, True)
