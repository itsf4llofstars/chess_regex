#!/usr/bin/env python3
"""Chess Regex Project main Python3 file"""
import menu as m
import os

good_dir: bool = False
while not good_dir:
    pgn_directory = m.get_pgn_dir()

    if not m.check_dir(pgn_directory):
        os.system('clear')
        print('Unable to find that path.\n')
        continue
    good_dir = True

good_file = False
