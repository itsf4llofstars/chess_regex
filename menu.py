#!/usr/bin/env python3.9
"""menu.py file for selecting pgn file actions"""
from os import system


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
    system("clear")

    print(options)
    return int(input())


def max_moves():
    system("clear")

    print("Enter the maximum number of games moves in ten's [4 returns games 39-moves and less]\n")
    return int(input("What is the maximum amount of moves you would like for your games: "))


if __name__ == "__main__":
    user_choice = display_options()
    print(user_choice)
    move_max = max_moves()
    print(move_max)

