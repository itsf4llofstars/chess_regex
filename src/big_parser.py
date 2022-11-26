"""
Initial write of big_parser.py the file that parses
all user selects in one function
"""
import re
import sys

regex_dict = {
    'legal_start': re.compile(r'^(1\.\s[a-hN][3-4acfh]3?\s[a-hN][5-6acfh]6?)'),
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
}


def parse_chess(path_file, game_endings, max_move):
    """This function parses all games at once since games
    file may be large. This is to mitigate memory issues.
    Research on parsing each single line in the with open
    section is needed, see python3 tips and tricks book.
    This as not been tried or tested
    """
    if game_endings == 8:
        sys.exit()
    elif game_endings == 1:
        regex = regex_dict['draws']
    elif game_endings == 2:
        regex = regex_dict['white_wins']
    elif game_endings == 3:
        regex = regex_dict['black_wins']
    elif game_endings == 4:
        regex = regex_dict['white_mates']
    elif game_endings == 5:
        regex = regex_dict['black_mates']
    elif game_endings == 6:
        regex = regex_dict['strip_white_mate']
    elif game_endings == 7:
        regex = regex_dict['strip_black_mate']

    regex_dict['max_moves'] = re.compile(r'\s[' + str(max_move) + r'-9]\d\.\s')

    games = []
    try:
        with open(path_file, 'r') as pgn_file:
            for game in pgn_file:
                if re.search(regex_dict['legal_start'], game) \
                        and not re.search(regex_dict['max_moves'], game) \
                        and not re.search(regex_dict['kibitz'], game):
                    if re.search(regex, game):
                        print(game)
    except FileNotFoundError as fnfe:
        print(f'Err: {fnfe}')  #! Logging
    return


def main():
    parse_chess('/home/bumper/chess/real_pgns_test.pgn', 2, 3)


if __name__ == '__main__':
    main()

