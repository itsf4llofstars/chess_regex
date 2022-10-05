#!/usr/bin/env python3
"""Chess Regex Project main Python3 file"""
import menu as m
import os

# Needed for F5 run of python scipt in Vim
os.system('clear')
os.system('clear')

pgn_directory = ''  # chess
good_dir: bool = False

while not good_dir:
    pgn_directory = m.get_pgn_dir()

    if not m.check_dir(pgn_directory):
        os.system('clear')
        print('Unable to find that path.\n')
        continue
    good_dir = True

del good_dir

pgn_file_name: str = ''  # pgn-one.pgn
good_file = False

while not good_file:
    pgn_file_name = m.get_pgn_file()

    if not m.check_file_exists(pgn_directory, pgn_file_name):
        os.system('clear')
        print('Unable to find that file.\n')
        continue
    good_file = True

del good_file

user_option: int = m.display_options()
if isinstance(user_option, int):
    print(user_option)
