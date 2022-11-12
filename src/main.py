#!/usr/bin/env python3
"""Chess Regex Project main Python3 file"""
import menu
import file_helper as fh
import pgn_parsers as parser
from sys import exit

# Call the menu.py dispaly options function to get
# the users game return choice.
users_choice = menu.display_options()

# Call menu.py get_pgn_dir function the get the users
# director[y|ies] where the pgn files are
pgn_path = menu.get_pgn_dir()

# Call menu.py get_pgn_file, passing the path variable
# to get the users pgn filename and join it with the
# path to the pgn file
pgn_path_file = menu.get_pgn_file(pgn_path)

maximum_moves = menu.max_moves()
maximum_moves = menu.set_max_move(maximum_moves)

raw_chess_games = fh.read_pgn_file(pgn_path_file)

only_games = parser.get_only_games(raw_chess_games)
del raw_chess_games

short_games = parser.no_long_games(only_games)
del only_games

games_list = []
if users_choice == 1:
    pass
elif users_choice == 2:
    parser.get_white_wins(short_games, games_list)
elif users_choice == 3:
    parser.get_black_wins(short_games, games_list)
elif users_choice == 4:
    parser.get_white_mates(short_games, games_list)
elif users_choice == 5:
    parser.get_black_mates(short_games, games_list)
elif users_choice == 6:
    exit()
