#!/usr/bin/env python3.9
"""menu.py file for selecting pgn file actions"""
import os
from sys import exit

OPTIONS = (
    '\n\tEnter the number for the option you would like to perform:\n\n'
    '\tReturn Games that:\n'
    '\t1) end in a draw\n'
    '\t2) White wins\n'
    '\t3) Black wins\n'
    '\t4) White Checkmates\n'
    '\t5) Black Checkmates\n'
    '\t6) Quit'
)


def display_options():
    while True:
        os.system('clear')
        print(OPTIONS)
        try:
            choice = int(input('\n\tChoice: '))
        except ValueError:
            print('\n\tPlease enter a number between 1 and 6.')
            input('\tContinue... ')
        else:
            if 0 < choice < 7:
                if choice == 6:
                    exit()
                return choice
            else:
                print('\n\tPlease enter a number between 1 and 6.')
                input('\tContinue... ')
                continue
    return


def get_pgn_dir():
    directory = ''
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


def check_dir(directory: str) -> bool:
    # return os.path.isdir(os.path.expanduser(os.path.join('~', directory)))
    return os.path.isdir(directory);


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

    return os.path.join('~', directory, file_name)


def check_file_exists(directory: str, pgn_file: str) -> bool:
    return os.path.isfile(os.path.expanduser(os.path.join('~', directory, pgn_file)))





def max_moves():
    os.system('clear')

    print("Enter the maximum number of game moves in ten's [4 returns games with 39-moves and less]\n")
    return int(input('What is the maximum amount of moves you would like for your games: '))


def set_max_move(number):
    if 2 >= number or number >= 9:
        print('Your max number of moves is to low or high\n'
              'Enter a number between 2 and 9 that represents\n'
              'the tens of moves.')
        return
    return number * 10


if __name__ == '__main__':
    user_choice = display_options()
    print(user_choice)

    max_move = max_moves()
    print(max_move)

    pgn_directory = get_pgn_dir()
    print(pgn_directory)

    pgn_file_name = get_pgn_file()
    print(pgn_file_name)

    if check_file_exists(pgn_directory, pgn_file_name):
        print('File exists')
