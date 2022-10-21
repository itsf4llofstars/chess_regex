#!/usr/bin/env python3
"""
This is a re-write of the project on branch bacon et. al.
bacon is NOT to be merged with main or any other branch
DO NOT MERGE
"""
import menu as mu
import pgn_parser as pgn
import os


if __name__ == '__main__':
    opera = ['1. e4 e5 2. Qf3', '1. e4 e5 2. Kf3', '1. e4 e5 2. f3']

    os.system('clear')

    mu.print_menu()
    users_choice: int = mu.get_user_choice()
    mu.check_choice(users_choice)

    pgn_path: str = pgn.get_path()
    full_path: str = pgn.expand_path(pgn_path)

    full_path_file: str = os.path.join(full_path, pgn.get_pgn_file())
    # full_path_file: str = os.path.join('/home/bumper/chess', 'bumper.pgn')
    pgn.check_path_file(full_path_file)

    pgn.get_only_games(opera)

    print('\n\n\tfin')

# DO NOT MERGE
