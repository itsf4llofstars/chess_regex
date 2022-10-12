#!/usr/bin/env python3
import os
import re

regex_dict = {
    'legal_start': re.compile(r'^(1\.\s[a-hN][3-4acfh]3?\s[a-hN][5-6acfh]6?)'),
    'no_forty': re.compile(r'\s[4-9]\d\.\s'),
    'no_hundred': re.compile(r'\s\d{3}\.\s'),
    'white_wins': re.compile(r'(\s1-0)$'),
    'black_wins': re.compile(r'(\s0-1)$'),
    'checkmate': re.compile(r'#'),
    'kibitz': re.compile(r'\s[(|{]'),
}


def check_path_format(path):
    """Checks the format of the passed path string. If The path
    does not start with a forward slash as forward slash is
    added to the beginning of the path. A Trailing slash is
    not required but can be passed

    Args:
        path (str): Path to the pgn file

    Returns:
        str: Path to the string
    """
    if not path.startswith('/'):
        path = '/' + path
    return path


def check_path_filename(path, filename):
    """Checks that the path exists and if it does joins the path
    to the filename. Checks if the path and file exists and
    returns the path and filename.

    Args:
        path (str): Path to the pgn file
        filename (str): pgn filename

    Returns:
        str: Full path joined to the filename
    """
    path_filename: str = ''

    if os.path.isdir(path):
        path_filename = os.path.join(path, filename)

    if os.path.isfile(path_filename):
        return path_filename

    return None


def read_pgn_file(full_path):
    """Reads in the pgn file and returns a list of lines stripped
    of their last char, which is a newline char.

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
        print(f'{fnfe}')
    except Exception as e:
        print(f'{e}')
    else:
        for line in pgn_file:
            lines_stripped.append(line.strip())
    finally:
        if len(lines_stripped):
            return lines_stripped
    return None


def get_only_games(chess_list):
    """Adds only those lines from a pgn that begin a chess games
    with a legal first move. Returns those games as a list.

    Args:
        chess_list (List[str]): List of lines from a pgn file

    Returns:
        List[str]: String list of only chess games
    """
    only_games = []
    for line in chess_list:
        if re.search(regex_dict['legal_start'], line):
            only_games.append(line)

    if len(only_games):
        return only_games
    return None


def no_long_games(chess_list):
    """Selects only those games that do not match the regex
    pattern to_long, appends them to a list. Returns a list of
    strings of games that are shorter than the to_long regex.

    Args:
        chess_list (List[str]): String list of games

    Returns:
        List[str]: String list of shorter games
    """
    short_games = []
    for game in chess_list:
        if not re.search(regex_dict['no_forty'], game) and not re.search(regex_dict['no_hundred'], game):
            short_games.append(game)

    if len(short_games):
        return short_games

    return None


def get_winner(chess_games_list, color, mate):
    """Appends to a winner list only those game whose winning
    color matches the wanted win color, and if mate is true
    appends those games what where won by checkmate

    Args:
        chess_games_list (List[str]: List of chess games
        color (str): The winning color to search for
        mate (bool): Append only those games with a hash in them

    Returns:
        List[str]: String list of winning color and mate
                   if wanted
    """
    winner = []
    for game in chess_games_list:
        if color.lower() == 'white':
            if re.search(regex_dict['white_wins'], game):
                if mate:
                    if re.search(regex_dict['checkmate'], game):
                        winner.append(game)
                elif not mate:
                    winner.append(game)
        elif color.lower() == 'black':
            if re.search(regex_dict['black_wins'], game):
                if mate:
                    if re.search(regex_dict['checkmate'], game):
                        winner.append(game)
                elif not mate:
                    winner.append(game)

    if len(winner):
        return winner
    return None


if __name__ == '__main__':
    os.system('clear')
    path_to_pgn = '/home/bumper/python/chess_regex/docs/pgn_test.pgn'
    pgn_file_lines = read_pgn_file(path_to_pgn)
    only_chess_games = get_only_games(pgn_file_lines)
    short_chess_games = no_long_games(only_chess_games)
    white_wins = get_winner(short_chess_games, 'white', False)
    black_wins = get_winner(short_chess_games, 'black', False)
    print(white_wins)
    print(black_wins)
