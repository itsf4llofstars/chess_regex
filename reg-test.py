#!/usr/bin/env python3
"""This is a test file only, it houses
the regex data to find certain games
"""
import os
import re
import menu as m

if __name__ == '__main__':
    pgn_file = []
    white_win = r'(\s1-0)$'
    black_win = r'(\s0-1)$'
    white_mates = r'(#\s1-0)$'
    black_mates = r'(#\s0-1)$'
    white_illeagal_move = r'^(1\.\s[a-hN][3-4acfh]3?)'
    black_illeagal_move = r'^(1\.\s[a-hN][3-4acfh]3?\s[a-hN][5-6acfh]6?)'
    no_forty = r'\s[4-9]\d\.\s'
    no_hundreds = r'\s\d{3}\.\s'
    no_sides_kibz_meta =r'[\[|{|(]'
    draws = r'(\s1/2-1/2)$'
    all_mates = r'(#\s[0-1]-[0-1]$)'

    with open('/home/bumper/python/chess_regex/regex_test.pgn', 'r') as f:
        for line in f:
            if not re.search(no_sides_kibz_meta, line) \
                    and not re.search(no_hundreds, line) \
                    and not re.search(no_forty, line):
                if re.search(black_illeagal_move, line) \
                        and re.search(white_win, line):
                    print(line)

