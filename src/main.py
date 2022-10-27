#!/usr/bin/env python3
"""Chess Regex Project main Python3 file"""
import menu

users_choice = menu.display_options()
pgn_path = menu.get_pgn_dir()
pgn_path_file = menu.get_pgn_file(pgn_path)

print('fin')

