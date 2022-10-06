#!/usr/bin/env python3.9
"""menu.py file for selecting pgn file actions"""
import os


def get_pgn_dir():
    print('Enter the directory of your chess pgn file:')
    print("If you directory is in '/home/$USER/chess/pgn_files', Enter: chess/pgn_files\n")
    return str(input())


def check_dir(directory: str) -> bool:
    return os.path.isdir(os.path.expanduser(os.path.join('~', directory)))


def get_pgn_file() -> str:
    print('Enter the name of the chess pgn file. .pgn is not required:')
    print('Example: chess-games[.pgn]\n')
    file_name: str = str(input())

    if not file_name.endswith('.pgn'):
        file_name += '.pgn'

    return file_name


def check_file_exists(directory: str, pgn_file: str) -> bool:
    return os.path.isfile(os.path.expanduser(os.path.join('~', directory, pgn_file)))


def display_options():
    # TODO: Error check 1 < input < 6
    while True:
        os.system('clear')
        options = (
            '\n\tEnter the number for the option you would like to perform:\n\n'
            '\tReturn Games:\n'
            '\t1) ending in a draw\n'
            '\t2) White wins\n'
            '\t3) Black wins\n'
            '\t4) White Checkmates\n'
            '\t5) Black Checkmates\n'
        )
        print(options)
        user_choice = input()
        if not isinstance(user_choice, int):
            return int(user_choice)
        print('Please enter an integer between 1 and 5\n')
        continue


def max_moves():
    os.system('clear')

    print("Enter the maximum number of game moves in ten's [4 returns games with 39-moves and less]\n")
    return int(input('What is the maximum amount of moves you would like for your games: '))


if __name__ == '__main__':
    user_choice = display_options()
    print(user_choice)
    move_max = max_moves()
    print(move_max)
