#!/usr/bin/env python3
"""Chess Regex Project main Python3 file"""
import menu as m

users_choice = m.display_options()

pgn_file_path = m.get_pgn_dir()
pgn_file_name = ''
if m.check_dir(pgn_file_path):
    pgn_file_name = m.get_pgn_file()
else:
    print('No directory')

if m.check_file_exists(pgn_file_path, pgn_file_name):
    print('YES')
else:
    print('No file')

max_num_moves = m.max_moves()
max_num_moves = m.set_max_move(max_num_moves)
print(max_num_moves)
