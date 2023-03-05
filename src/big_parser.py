# Initial write of big_parser.py the file that parses
# all user selects in one function
import os

file_name = os.path.expanduser(os.path.join('~', 'chess', 'bumper.pgn'))
max_move = ' 40. '
games = []

with open(file_name, 'r') as fo:
    for line in fo:
        line = line.strip()
        if (
                not line.startswith('1. ')
                or not line[-2] == '-'
                or '(' in line
                     or ')' in line
                or '{' in line
                     or '}' in line
                or max_move in line
                ):
            continue
        line = line.replace('!', '')
        line = line.replace('!!', '')
        line = line.replace('?', '')
        line = line.replace('??', '')
        line = line.replace('?!', '')
        line = line.replace('!?', '')
        line = line.replace('+', '')
