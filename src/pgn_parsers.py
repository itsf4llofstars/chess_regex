#!/usr/bin/env python3
import os
import re
import sys

regex_dict = {
    'legal_start': re.compile(r'^(1\.\s[a-hN][3-4acfh]3?\s[a-hN][5-6acfh]6?)'),
    'no_forty': re.compile(r'\s[4-9]\d\.\s'),
    'no_hundred': re.compile(r'\s\d{3}\.\s'),
    'white_wins': re.compile(r'(\s1-0)$'),
    'black_wins': re.compile(r'(\s0-1)$'),
    'white_mates': re.compile(r'(#\s1-0)$'),
    'black_mates': re.compile(r'(#\s0-1)$'),
    'kibitz': re.compile(r'\s[(|{]'),
}


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

def get_white_wins(chess_games, winner):
    """Accepts a list of chess games and searches for the
    white_wins regex. Appends the game if the regex white_wins
    is found in the game.

    Args:
        chess_games: list[str] List of chess games to be searched
        winner: list[str]: List to be populated with white's wins
    """
    for game in chess_games:
        if re.search(regex_dict['white_wins'], game):
            winner.append(game)


def get_white_mates(chess_games, winner):
    """Accepts a list of chess games and searches for the
    white_mates regex. Appends the game if the regex white_mates
    is found in the game.

    Args:
        chess_games: list[str] List of chess games to be searched
        winner: list[str]: List to be populated with white's wins
    """
    for game in chess_games:
        if re.search(regex_dict['white_mates'], game):
            winner.append(game)


def get_black_wins(chess_games, winner):
    """Accepts a list of chess games and searches for the
    black_wins regex. Appends the game if the regex black_wins
    is found in the game.

    Args:
        chess_games: list[str] List of chess games to be searched
        winner: list[str]: List to be populated with black's wins
    """
    for game in chess_games:
        if re.search(regex_dict['black_wins'], game):
            winner.append(game)


def black_mates(chess_games, color):
    return None


if __name__ == '__main__':
    games = []
    with open('/home/bumper/chess/games1.pgn', 'r') as fo:
        games = fo.readlines()

    strip_games = []
    for game in games:
        strip_games.append(game.strip())

    raw_games = get_only_games(strip_games)
    short_games = no_long_games(raw_games)

    # White wins function
    white_won = []
    get_white_wins(short_games, white_won)

    # Black wins function
    black_won = []
    get_black_wins(short_games, black_won)

    # White mates function
    white_mates = []
    get_white_mates(short_games, white_mates)

    [print(game) for game in white_mates]

