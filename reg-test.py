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

#     white_mates = r'(#\s1-0)$'
#     for line in pgn_file:
#         if re.search(white_mates, line):
#             print(line)
#
#     black_mates = r'(#\s0-1)$'
#     for line in pgn_file:
#         if re.search(black_mates, line):
#             print(line)

#     white_illeagal_move = r'^(1\.\s[a-hN][3-4acfh]3?)'
#     black_illeagal_move = r'^(1\.\s[a-hN][3-4acfh]3?\s[a-hN][5-6acfh]6?)'
#     for line in pgn_file:
#         if re.search(black_illeagal_move, line):
#         # if re.search(white_illeagal_move, line):
#             print(line)

#     no_forty = r'\s[4-9]\d\.\s'
#     no_hundreds = r'\s\d{3}\.\s'
#     for line in pgn_file:
#         if re.search(no_forty, line) or re.search(no_hundreds, line):
#             continue
#         print(line)

#     no_sides_kibz_meta =r'[\[|{|(]'
#     for line in pgn_file:
#         if not re.search(no_sides_kibz_meta, line):
#             print(line)

#     draws = r'(\s1/2-1/2)$'
#     for line in pgn_file:
#         if re.search(draws, line):
#             print(line)

    all_mates = r'(#\s[0-1]-[0-1]$)'
    for line in pgn_file:
        if re.search(all_mates, line):
            print(line)
