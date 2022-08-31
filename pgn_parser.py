#!/usr/bin/env python3
import os
import re


def check_path_format(path):
    """Checks the format of the passed path string.
    If The path does not start with a forward slash
    as forward slash is added to the beginning of the
    path. A Trailing slash is not required but can be
    passed

    Args:
        path (str): Path to the pgn file

    Returns:
        str: Path to the string
    """
    if not path.startswith('/'):
        path = '/' + path
    return path


def check_path_filename(path, filename):
    path_filename: str = None

    if os.path.isdir(path):
        path_filename = os.path.join(path, filename)

    if os.path.isfile(path_filename):
        return path_filename

    return None


if __name__ == "__main__":
    file_path = "home/bumper/python/chess_regex"
    filename = "test-chess.pgn"
    file_path = check_path_format(file_path)

    full_path = check_path_filename(file_path, filename)
    print(full_path)
