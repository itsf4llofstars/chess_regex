"""
Initial write of big_parser.py the file that parses
all user selects in one function
"""
import re
import sys
from random import choice

regex_dict = {
    'legal_start': re.compile(r'^(1\.\s[a-hN].+[a-hN].+\.\s)'),
    'max_move': re.compile(r'\s[4-9]\d\.\s'),
    'max_moves': '',
    'no_hundred': re.compile(r'\s\d{3}\.\s'),
    'white_wins': re.compile(r'(\s1-0)$'),
    'black_wins': re.compile(r'(\s0-1)$'),
    'white_mates': re.compile(r'(#\s1-0)$'),
    'black_mates': re.compile(r'(#\s0-1)$'),
    'kibitz': re.compile(r'\s[(|{]'),
    'strip_white_mate': re.compile(r'\s\d{1,2}\.\s\w+=?[B-R]?#\s1-0'),
    'strip_black_mate': re.compile(r'\s\w+=?[B-R]?#\s0-1'),
    'annotates': re.compile(r'[!|!!|?|??|?!|!?]'),
}


def parse_chess(path_file, game_endings, max_move, random_choice):
    """This function parses all games at once since games
    file may be large. This is to mitigate memory issues.
    Research on parsing each single line in the with open
    section is needed, see python3 tips and tricks book.
    This as not been tried or tested
    """

    regex_dict['max_moves'] = re.compile(r'\s[' + str(max_move) + r'\-9]\d\.\s')

    games = []
    with open(path_file, 'r') as pgn_file:
        for game in pgn_file:
            if not game.startswith('1. ') or '(' in game or ')' in game or '{' in game or '}' in game:
                continue


def main():
    random_game = True
    chess_games = parse_chess('/home/bumper/python/chess_regex/docs/opera_test.pgn', 3, 3, random_game)
    if random_game:
        print(chess_games)
    else:
        [print(game) for game in chess_games]


if __name__ == '__main__':
    main()
