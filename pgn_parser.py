#!/usr/bin/env python3
import os
import re

regex_dict = {
    "legal_start": r"1\.\s[1-hN][1-3acfg]3?\s[a-hN][6-5acfh]6?\s",
    "to_long": r"[1-9]?[4-9]\d\.\s",
    "white_wins": r"(\s1-0)$",
    "black_wins": r"(\s0-1)$",
    "white_mates": r"(#\s1-0)$",
    "black_mates": r"(#\s0-1)$",
    "kibitz": r"\s[(|{]",
}


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
    """Checks that the path exists and if it
    does joins the path to the filename. Checks
    if the path and file exists and returns
    the path and filename.

    Args:
        path (str): Path to the pgn file
        filename (str): pgn filename

    Returns:
        str: Full path joined to the filename
    """
    path_filename: str = None

    if os.path.isdir(path):
        path_filename = os.path.join(path, filename)

    if os.path.isfile(path_filename):
        return path_filename

    return None


def read_pgn_file(full_path):
    """Reads in the pgn file and returns a list
    of lines stripped of their last char, which
    is a newline char.

    Args:
        full_path (str): Full path with filename

    Returns:
        List[str]: A list of line from the pgn file.
    """
    lines_stripped = []

    try:
        with open(full_path, 'r') as fo:
            pgn_file = fo.readlines()
    except FileNotFoundError as fnfe:
        print(f"{fnfe}")
    except Exception as e:
        print(f"{e}")
    else:
        for line in pgn_file:
            lines_stripped.append(line.strip())
    finally:
        if len(lines_stripped):
            return lines_stripped
    return None


if __name__ == "__main__":
    file_path = "home/bumper/python/chess_regex"
    filename = "test-chess.pgn"

    file_path = check_path_format(file_path)
    path_file = check_path_filename(file_path, filename)
    chess_pgn = read_pgn_file(path_file)

    [print(line) for line in chess_pgn]
