#!/usr/bin/env python3
"""pgn_parsers.py"""
import re
from random import choice

# max_moves = 6

regex_dict = {
    "legal_start": re.compile(r"^(1\.\s[a-hN])"),
    "max_move": re.compile(r"\s[4-9]\d\.\s"),
    "max_moves": "",
    "no_hundred": re.compile(r"\s\d{3}\.\s"),
    "white_wins": re.compile(r"(\s1-0)$"),
    "black_wins": re.compile(r"(\s0-1)$"),
    "white_mates": re.compile(r"(#\s1-0)$"),
    "black_mates": re.compile(r"(#\s0-1)$"),
    "kibitz": re.compile(r"\s[(|{]"),
    "strip_white_mate": re.compile(r"\s\d{1,2}\.\s\w+=?[B-R]?#\s1-0"),
    "strip_black_mate": re.compile(r"\s\w+=?[B-R]?#\s0-1"),
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
        if re.search(regex_dict["legal_start"], line):
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
        if not re.search(regex_dict["max_moves"], a_game) and not re.search(
            regex_dict["no_hundred"], a_game
        ):
            shorts.append(a_game)

    if len(shorts):
        return shorts

    return


def omit_kibitz_games(chess_list):
    """Doc"""
    clean_games = []
    for a_game in chess_list:
        if re.search(regex_dict["kibitz"], a_game):
            continue
        clean_games.append(a_game)

    if len(clean_games):
        return clean_games
    return


def replace_tags(tagged_games):
    """Removes the move annotaion tags and check tag
    !, !!, ?, ??, !?, ?!, - and + from the end of moves

    Args:
        tagged_games [list(str)]: The list of chess games

    Returns:
        not_tagged [list(str)]: List of chess games sans tags
    """
    not_tagged = []
    for a_game in tagged_games:
        a_game = a_game.replace("!", "")
        a_game = a_game.replace("?", "")
        a_game = a_game.replace("+-", "")
        a_game = a_game.replace("-+", "")
        a_game = a_game.replace("+", "")
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
        if re.search(regex_dict["white_wins"], a_game):
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
        if re.search(regex_dict["white_mates"], a_game):
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
        if re.search(regex_dict["black_wins"], a_game):
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
        if re.search(regex_dict["black_mates"], a_game):
            winner.append(a_game)


def strip_white_mates(chess_games, no_mates):
    """DOC"""
    for a_game in chess_games:
        if re.search(regex_dict["white_mates"], a_game):
            no_mate_str = re.sub(regex_dict["strip_white_mate"], "", a_game)
            no_mates.append(no_mate_str)


def strip_black_mates(chess_games, no_mates):
    """DOC"""
    for a_game in chess_games:
        if re.search(regex_dict["black_mates"], a_game):
            no_mate_str = re.sub(regex_dict["strip_black_mate"], "", a_game)
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
    return random_chess_game.split(" ")


def set_max_move(number):
    """Doc"""
    regex_dict["max_moves"] = re.compile(r"\s[" + str(number) + r"\-9]\d\.\s")
    # r"\s[4-9]\d\.\s"


if __name__ == "__main__":
    long_games = [
        "1.e4 e5 1.e4 e5 1.e4 e5 1.e4 e5 1.e4 e5 1.e4 e5",
        "2.e4 e5 1.e4 e5 1.e4 e5 39.e4 e5 1.e4 e5 1.e4 e5",
        "3.e4 e5 1.e4 e5 1.e4 e5 40.e4 e5 1.e4 e5 1.e4 e5",
        "4.e4 e5 1.e4 e5 40.e4 e5 56.e4 e5 1.e4 e5 1.e4 e5",
    ]

    short_games = no_long_games(long_games)
    [print(game) for game in short_games]
