# Initial write of big_parser.py the file that parses
# all user selects in one function
import os
import random
import re

file_name = os.path.expanduser(os.path.join('~', 'chess', 'bumper.pgn'))
min_move = ' 10. '
max_move = ' 40. '
white = False
mate = True

# Second white move not tested
legal_start = re.compile(r'^(1\.\s[a-hN][3-4acfh]3?\s[a-hN][5-6acfh]6?\s2\.\s[a-hBNKQR][1-6a-h])')

games = []

with open(file_name, 'r') as fo:
    for line in fo:
        if (
                not line.startswith('1. ')
                or max_move in line
                or min_move not in line
                or not line[-3] == '-'
                or not min_move in line
                or '(' in line
                     or ')' in line
                or '{' in line
                     or '}' in line
                or '[' in line
                     or ']' in line
                ):
            continue
        elif not re.search(legal_start, line):
            continue
        line = line.replace('!', '')
        line = line.replace('!!', '')
        line = line.replace('?', '')
        line = line.replace('??', '')
        line = line.replace('?!', '')
        line = line.replace('!?', '')
        line = line.replace('+', '')
        line = line.rstrip()

os.system('clear')
chess_game = random.choice(games)
print(chess_game)
print()
print(f'{len(games)} games.')
