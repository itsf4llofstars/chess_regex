"""
This is a re-write of the project on branch bacon et. al.
bacon is NOT to be merged with main or any other branch
DO NOT MERGE
"""
import os
from sys import exit


def get_path():
    os.system('clear')

    print('''\n\n\tThe path to the pgn file should be entered without the leading
\t~/ and or without the leading /home/$USER/ Enter the path as path/to/pgn/file.\n''')
    return str(input('\tEnter the path to the pgn file: '))


def check_path(path_pgn: str) -> str:
    if not os.path.isdir(os.path.expanduser(os.path.join('~', path_pgn))):
        print('The path could not be found.')
        exit()

    return os.path.expanduser(os.path.join('~', path_pgn))


if __name__ == '__main__':
    pass

# DO NOT MERGE
