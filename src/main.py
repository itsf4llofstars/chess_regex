#!/usr/bin/env python3
"""Chess Regex Project main Python3 file"""
import menu
import file_helper as fh

users_choice = menu.display_options()
pgn_path = menu.get_pgn_dir()
pgn_path_file = menu.get_pgn_file(pgn_path)
maximum_moves = menu.max_moves()
maximum_moves = menu.set_max_move(maximum_moves)
