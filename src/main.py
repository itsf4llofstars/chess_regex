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
import random

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

del games

# Omit kibitz ( { [ <
paren_o = "("
paren_c = ")"
brace_o = "{"
brace_c = "}"
bracket_o = "["
bracket_c = "]"
tag_o = "<"
tag_c = ">"
no_kibitz = []
for game in move_games:
    if (
        paren_o in game
        or paren_c in game
        or brace_o in game
        or brace_c in game
        or bracket_o in game
        or bracket_c in game
        or tag_o in game
        or tag_c in game
    ):
        continue
    no_kibitz.append(game)

del move_games

# Git wins and mates
white = True
mate = True
white_win = " 1-0"
black_win = " 0-1"
mate_hash = "#"
winner = []

for game in no_kibitz:
    if white and mate:
        if game.endswith(white_win) and mate_hash in game:
            winner.append(game)
    elif white and not mate:
        if game.endswith(white_win) and mate_hash not in game:
            winner.append(game)
    elif not white and mate:
        if game.endswith(black_win) and mate_hash in game:
            winner.append(game)
    elif not white and not mate:
        if game.endswith(black_win) and mate_hash not in game:
            winner.append(game)

del no_kibitz

random_game = random.choice(winner)
print(random_game)
