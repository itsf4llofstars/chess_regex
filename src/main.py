#!/usr/bin/env python3
"""
This is a re-write of the project on branch bacon et. al.
bacon is NOT to be merged with main or any other branch
DO NOT MERGE
"""
import menu as mu
import pgn_parser as pgn
from os import system

if __name__ == '__main__':
    system('clear')

    mu.print_menu()
    users_choice: int = mu.get_user_choice()
    mu.check_choice(users_choice)

    pgn_path: str = pgn.get_path()

    print('\n\n\tfin')

# DO NOT MERGE
