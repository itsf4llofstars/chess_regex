#!/usr/bin/env python3
"""main.py
This file on the fastest git branch is
explained in the fastest_branch.md file

Straight through. Little regex as possible.
Full File read into list, appending to a new
list and deleting the old as we go.
pgn file size is 1GB, with approx 500,000+ chess games
read form a 32GB micro-SD card.
"""
import os

file_name = "lichess_short.pgn"
pgn_file = os.path.expanduser(
    # os.path.join("/media", "bumper", "EDD2-E40F", "raspi32", file_name)
    os.path.join("~", "python", "chess_regex", "docs", "regex_test.pgn")
)

# Read in the file
pgn_lines = []
with open(pgn_file) as read:
    pgn_lines = read.readlines()

# Get only those games starting with 1._
games = []
start_str = "1. "
for line in pgn_lines:
    if line.startswith(start_str):
        games.append(line.rstrip())

del pgn_lines

# Get games with 20 - 40 move
max_move = " 40. "
min_move = " 20. "
move_games = []
for game in games:
    if min_move in game and max_move not in game:
        move_games.append(game)

[print(game) for game in games]
print(len(games))
input("Cont ONE...")
del games


[print(game) for game in move_games]
print(len(move_games))
input("Cont TWO...")
