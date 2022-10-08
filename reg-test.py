#!/usr/bin/env python3
"""This is a test file only, it houses
the regex data to find certain games
"""
import re
import menu as m

if __name__ == '__main__':
    pgn_file = []
    with open('/home/bumper/chess/pgn-one.pgn', 'r') as fo:
        pgn_data = fo.readlines()
        for line in pgn_data:
            pgn_file.append(line.strip())

#     white_win = r'(\s1-0)$'
#     for line in pgn_file:
#         if re.search(white_win, line):
#             print(line)
#
#     black_win = r'(\s0-1)$'
#     for line in pgn_file:
#         if re.search(black_win, line):
#             print(line)

    white_mates = r'(#\s1-0)$'
    for line in pgn_file:
        if re.search(white_mates, line):
            print(line)

