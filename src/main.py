#!/usr/bin/env python3
"""Chess Regex Project main Python3 file"""
import menu
import file_helper

users_choice = menu.display_options()
pgn_path = menu.get_pgn_dir()
pgn_path_file = menu.get_pgn_file(pgn_path)

raw_chess_games = file_helper.read_pgn_file(pgn_path_file)
file_helper.write_file('/home/bumper/python/chess_regex/src/test_games.pgn', raw_chess_games)
[print(game) for game in raw_chess_games]

