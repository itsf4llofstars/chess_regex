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
        line = line.rstrip()
        if (
                not line.startswith('1. ')
                or not line[-2] == '-'
                or not min_move in line
                or '(' in line
                     or ')' in line
                or '{' in line
                     or '}' in line
                or '[' in line
                     or ']' in line
                or max_move in line
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
        if white and line.endswith(' 1-0'):
            if mate and '#' in line:
                games.append(line)
            elif not mate and '#' not in line:
                games.append(line)
        elif not white and line.endswith(' 0-1'):
            if mate and '#' in line:
                games.append(line)
            elif not mate and '#' not in line:
                games.append(line)

[print(game) for game in games]
chess_game = random.choice(games)
print()
print(chess_game)
print()
print(len(games))
