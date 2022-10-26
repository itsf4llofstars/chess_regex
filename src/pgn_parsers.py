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

def white_wins():
    return None


def white_mates(chess_games, color):
    return None


def black_wins():
    return None


def black_mates(chess_games, color):
    return None


if __name__ == '__main__':
    pass

