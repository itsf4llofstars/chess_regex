"""
Initial write of big_parser.py the file that parses
all user selects in one function
"""
import re
import sys

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
    if game_endings == 8:
        sys.exit()

    regex_dict['max_moves'] = re.compile(r'\s[' + str(max_move) + r'-9]\d\.\s')

    games = []
    try:
        with open(path_file, 'r') as fo:
            lines = fo.readlines()
    except FileNotFoundError as fnfe:
        print(f'Err: {fnfe}')  #! Logging
    else:
        for line in lines:
            if re.search(regex_dict['legal_start'], line) \
                    and not re.search(regex_dict['max_moves'], line) \
                    and not re.search(regex_dict['kibitz'], line:
                if game_endings == 1:
                    # if re.search(regex_dict[''], line):
                    #     games.append(line)
                    pass
                if game_endings == 2:
                    if re.search(regex_dict['white_wins'], line):
                        games.append(line)
                if game_endings == 3:
                    if re.search(regex_dict['black_wins'], line):
                        games.append(line)
                if game_endings == 4:
                    if re.search(regex_dict['white_mates'], line):
                        games.append(line)
                if game_endings == 5:
                    if re.search(regex_dict['black_mates'], line):
                        games.append(line)
                if game_endings == 6:
                    if re.search(regex_dict['strip_white_mates'], line):
                        games.append(line)
                if game_endings == 7:
                    if re.search(regex_dict['strip_black_mates'], line):
                        games.append(line)
            else:
                continue
    finally:
        if len(games):
            return games
    return


def main():
    pass


if __name__ == '__main__':
    main()

