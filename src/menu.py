#!/usr/bin/env python3.9
"""menu.py file for selecting pgn file actions"""
import os
import pgn_parsers as pgnp
from sys import exit

OPTIONS = (
    '\n\tEnter the number for the option you would like to perform:\n\n'
    '\tReturn Games that:\n'
    '\t1) end in a draw\n'
    '\t2) White wins\n'
    '\t3) Black wins\n'
    '\t4) White Checkmates\n'
    '\t5) Black Checkmates\n'
    "\t6) Strip White's Checkmate\n"
    "\t7) Strip Black's Checkmate\n"
    '\t8) Quit'
)


def display_options():
    while True:
        os.system('clear')
        print(OPTIONS)
        try:
            choice = int(input('\n\tChoice: '))
        except ValueError:
            print('\n\tPlease enter a number between 1 and 8.')
            input('\tContinue... ')
        else:
            if 0 < choice < 9:
                if choice == 8:
                    exit()
                return choice
            else:
                print('\n\tPlease enter a number between 1 and 8.')
                input('\tContinue... ')
                continue
    return


def get_pgn_dir():
    while True:
        print('\tEnter the directory of your chess pgn file:')
        print("\tIf your directory is '/home/$USER/chess/pgn_files', Enter: chess/pgn_files\n")
        directory = str(input('\t'))

        if not os.path.isdir(os.path.expanduser(os.path.join('~', directory))):
            print(f'\tThe directory {directory} could not be found')
            input('\tEnter to retry... ')
            os.system('clear')
            continue
        else:
            break

    return os.path.expanduser(os.path.join('~', directory))


def check_dir(directory: str):
    """Deprecated: 2022-11-04
    check_dir is still actively being tested under
    tests
    """
    return os.path.expanduser(os.path.join('~', directory))


def get_pgn_file(directory: str) -> str:
    while True:
        print('\tEnter the name of the chess pgn file. .pgn is optional:')
        print('\tExample: chess-games[.pgn]\n')
        file_name: str = str(input('\t'))

        if not file_name.endswith('.pgn'):
            file_name += '.pgn'

        if not os.path.isfile(os.path.join(directory, file_name)):
            print(f'\tThe file {file_name} could not be found')
            input('\tEnter to retry... ')
            os.system('clear')
            continue
        else:
            break

    return os.path.join(directory, file_name)


def check_file_exists(directory: str, file_name: str):
    return os.path.join(directory, file_name)


def max_moves():
    os.system('clear')
    max_moves = 0
    while max_moves < 1 or max_moves > 9:
        print(
            "\nEnter the maximum number of game moves in ten's [4 returns games with 49-moves and less]\n",
            "\bYou can enter move numbers up to 9, which would return games of 99-moves and less.\n",
            "\bThe minimum number is 1, 19-moves and less.\n"
        )
        max_moves = int(input('\nWhat is the maximum amount of moves you would like for your games: '))

    return max_moves


def set_max_move(number):
    """Doc
    """
    pgnp.max_moves = number


if __name__ == '__main__':
    user_choice = display_options()
    print(user_choice)

    max_move = max_moves()
    print(max_move)

    pgn_directory = get_pgn_dir()
    print(pgn_directory)

    pgn_file_name = get_pgn_file(pgn_directory)
    print(pgn_file_name)

    if check_file_exists(pgn_directory, pgn_file_name):
        print('File exists')
