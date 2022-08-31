#!/usr/bin/env python3.9
"""menu.py file for selecting pgn file actions"""
import os


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


if __name__ == "__main__":
    user_choice = display_options()
    print(user_choice)

