#!/usr/bin/env python3.9
"""menu.py file for selecting pgn file actions"""
import os


def get_pgn_dir():
    print("Enter the directory of your chess pgn file:")
    print("Example: chess/pgn_files\n")
    return str(input())


def check_dir(directory: str) -> bool:
    return os.path.isdir(os.path.expanduser(os.path.join('~', directory)))


def display_options():
    options = (
        "Enter the number for the option you would like to perform:\n\n"
        "Return Games:\n"
        "1) ending in a draw\n"
        "2) White wins\n"
        "3) Black wins\n"
        "4) White Checkmates\n"
        "5) Black Checkmates\n"
    )
    os.system("clear")

    print(options)
    return int(input())


def max_moves():
    os.system("clear")

    print("Enter the maximum number of game moves in ten's [4 returns games with 39-moves and less]\n")
    return int(input("What is the maximum amount of moves you would like for your games: "))


if __name__ == "__main__":
    user_choice = display_options()
    print(user_choice)
    move_max = max_moves()
    print(move_max)
