#!/usr/bin/env python3
"""Chess Regex Project main Python3 file"""
import menu
import file_helper as fh
import pgn_parsers as parser
from sys import exit

"""Call the menu.py display options function to get
the users game return choice."""
users_choice = menu.display_options()

"""Call menu.py get_pgn_dir function the get the users
director[y|ies] where the pgn files are"""
pgn_path = menu.get_pgn_dir()

"""Call menu.py get_pgn_file, passing the path variable
to get the users pgn filename and join it with the"""
# path to the pgn file
pgn_path_file = menu.get_pgn_file(pgn_path)

"""Call the menu.py max_moves function to get the maximum
number of moves the user wants for the their game
These max moves are not currently
in use."""
maximum_moves = menu.max_moves()

"""Set the maximum_moves variable for numeric validity
and return it as a string for use in the regex dict in
pgn_parsers.py file. These max moves are not currently
in use."""
maximum_moves = menu.set_max_move(maximum_moves)

"""Get the pgn files raw data"""
raw_chess_games = fh.read_pgn_file(pgn_path_file)

"""Parse out only the chess games"""
only_games = parser.get_only_games(raw_chess_games)
del raw_chess_games

"""Parse out only those games what match the length the
user requested. As of now it is set to games no greater
than 39 moves."""
short_games = parser.no_long_games(only_games)
del only_games

"""Parse out only those games that meet the users choice
of winning criteria"""
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

print(games_list)
input('Continue... ')

study_game = parser.pick_one_game(games_list)
del games_list
print(study_game)
