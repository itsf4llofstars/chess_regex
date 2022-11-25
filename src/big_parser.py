"""
Initial write of big_parser.py the file that parses
all user selects in one function
"""
import re

regex_dict = {
    'legal_start': re.compile(r'^(1\.\s[a-hN][3-4acfh]3?\s[a-hN][5-6acfh]6?)'),
    'max_move': re.compile(r'\s[4-9]\d\.\s'),
    'max_moves': '',  #! This is set from menu.py
    'no_hundred': re.compile(r'\s\d{3}\.\s'),
    'white_wins': re.compile(r'(\s1-0)$'),
    'black_wins': re.compile(r'(\s0-1)$'),
    'white_mates': re.compile(r'(#\s1-0)$'),
    'black_mates': re.compile(r'(#\s0-1)$'),
    'kibitz': re.compile(r'\s[(|{]'),
    'strip_white_mate': re.compile(r'\s\d{1,2}\.\s\w+=?[B-R]?#\s1-0'),
    'strip_black_mate': re.compile(r'\s\w+=?[B-R]?#\s0-1'),
}


def parse_chess(path_file, game_endings, max_move):
    try:
        pass
    except:
        pass
    else:
        pass
    finally:
        pass


def main():
    pass


if __name__ == '__main__':
    main()

