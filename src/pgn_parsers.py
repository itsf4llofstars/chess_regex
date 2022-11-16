#!/usr/bin/env python3
"""pgn_parsers.py"""
import re
from random import choice

max_moves = 6

regex_dict = {
    'legal_start': re.compile(r'^(1\.\s[a-hN][3-4acfh]3?\s[a-hN][5-6acfh]6?)'),
    'max_move': re.compile(r'\s[4-9]\d\.\s'),
    'max_moves': re.compile(r'\s[' + str(max_moves) + r'\-9]\d\.\s'),
    'no_hundred': re.compile(r'\s\d{3}\.\s'),
    'white_wins': re.compile(r'(\s1-0)$'),
    'black_wins': re.compile(r'(\s0-1)$'),
    'white_mates': re.compile(r'(#\s1-0)$'),
    'black_mates': re.compile(r'(#\s0-1)$'),
    'kibitz': re.compile(r'\s[(|{]'),
    'strip_white_mate': re.compile(r'\s\d{1,2}\.\s\w+=?[B-R]?#\s1-0'),
    'strip_black_mate': re.compile(r'\s\w+=?[B-R]?#\s0-1'),
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
    shorts = []
    for a_game in chess_list:
        if not re.search(regex_dict['max_move'], a_game) and not re.search(regex_dict['no_hundred'], a_game):
            shorts.append(a_game)

    if len(shorts):
        return shorts

    return


def omit_kibitz_games(chess_list):
    """Doc
    """
    clean_games = []
    for a_game in chess_list:
        if re.search(regex_dict['kibitz'], a_game):
            continue
        clean_games.append(a_game)

    if len(clean_games):
        return clean_games
    return


def replace_tags(tagged_games):
    """The order of the replace function must remain.
    !! and ?? are replaced on the ! and ? calls but best
    to leave them in
    """
    not_tagged = []
    for a_game in tagged_games:
        a_game = a_game.replace('!', '')
        a_game = a_game.replace('!!', '')
        a_game = a_game.replace('?', '')
        a_game = a_game.replace('??', '')
        a_game = a_game.replace('!?', '')
        a_game = a_game.replace('?!', '')
        a_game = a_game.replace('-+', '')
        a_game = a_game.replace('+-', '')
        a_game = a_game.replace('+', '')
        not_tagged.append(a_game)
    return not_tagged


def get_white_wins(chess_games, winner):
    """Accepts a list of chess games and searches for the
    white_wins regex. Appends the game if the regex white_wins
    is found in the game.

    Args:
        chess_games: list[str] List of chess games to be searched
        winner: list[str]: List to be populated with white's wins
    """
    for a_game in chess_games:
        if re.search(regex_dict['white_wins'], a_game):
            winner.append(a_game)


def get_white_mates(chess_games, winner):
    """Accepts a list of chess games and searches for the
    white_mates regex. Appends the game if the regex white_mates
    is found in the game.

    Args:
        chess_games: list[str] List of chess games to be searched
        winner: list[str]: List to be populated with white's wins
    """
    for a_game in chess_games:
        if re.search(regex_dict['white_mates'], a_game):
            winner.append(a_game)


def get_black_wins(chess_games, winner):
    """Accepts a list of chess games and searches for the
    black_wins regex. Appends the game if the regex black_wins
    is found in the game.

    Args:
        chess_games: list[str] List of chess games to be searched
        winner: list[str]: List to be populated with black's wins
    """
    for a_game in chess_games:
        if re.search(regex_dict['black_wins'], a_game):
            winner.append(a_game)


def get_black_mates(chess_games, winner):
    """Accepts a list of chess games and searches for the
    black_mates regex. Appends the game if the regex black_mates
    is found in the game.

    Args:
        chess_games: list[str] List of chess games to be searched
        winner: list[str]: List to be populated with black's wins
    """
    for a_game in chess_games:
        if re.search(regex_dict['black_mates'], a_game):
            winner.append(a_game)


def strip_white_mates(chess_games, no_mates):
    """DOC
    """
    for a_game in chess_games:
        if re.search(regex_dict['white_mates'], a_game):
            no_mate_str = re.sub(regex_dict['strip_white_mate'], '', a_game)
            no_mates.append(no_mate_str)


def strip_black_mates(chess_games, no_mates):
    """DOC
    """
    for a_game in chess_games:
        if re.search(regex_dict['black_mates'], a_game):
            no_mate_str = re.sub(regex_dict['strip_black_mate'], '', a_game)
            no_mates.append(no_mate_str)


def pick_one_game(chess_games):
    """Returns a list of individual moves and move
    numbers form a randomly chosen game from chess_games

    Args:
        chess_games: List of chess games

    Returns:
        List of individual strings for each move
        and move number
    """
    random_chess_game = choice(chess_games)
    return random_chess_game.split(' ')


if __name__ == '__main__':
    """
    # games = []
    with open('/home/bumper/chess/real_pgns_test.pgn', 'r') as fo:
        games = fo.readlines()

    strip_games = []
    for game in games:
        strip_games.append(game.strip())

    tagged_games_list = [
        "1. c4 d5! 2. Nf3!! d6? 12. d4?? d4?! 12. d4!? d4+- 12. d4-+ d4+ 1-0"
    ]

    foo = replace_tags(tagged_games_list)
    print(foo)

    raw_games = get_only_games(strip_games)
    short_games = no_long_games(raw_games)
    no_kibitz = omit_kibitz_games(short_games)
    tags_games = replace_tags(no_kibitz)
    audio_game = pick_one_game(tags_games)
    print(audio_game)

    # White wins function
    white_won = []
    get_white_wins(short_games, white_won)

    # Black wins function
    black_won = []
    get_black_wins(short_games, black_won)

    # White mates function
    white_mates = []
    get_white_mates(short_games, white_mates)

    # Black mates function
    black_mates = []
    get_black_mates(short_games, black_mates)

    # No White Mates
    no_white_mates = []
    strip_white_mates(short_games, no_white_mates)
    [print(game) for game in short_games]
    [print(wins) for wins in no_white_mates]

    no_black_mates = []
    strip_black_mates(short_games, no_black_mates)
    [print(game) for game in short_games]
    [print(wins) for wins in no_black_mates]

    print(white_won[-1])
    print(black_won[-1])
    print(white_mates[-1])
    print(black_mates[-1])
    [print(game) for game in black_mates]
    """

    for v in regex_dict.values():
        print(v)
