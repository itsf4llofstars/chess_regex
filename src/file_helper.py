"""File Operations File"""
import re


def read_pgn_file(path_file):
    pgn_games = []
    try:
        with open(path_file, 'r') as fo:
            pgn_lines = fo.readlines()
    except FileNotFoundError as fnfe:
        # TODO: Setup logging
        print(f'{fnfe}')
    else:
        start = re.compile(r'1\.\s')
        for line in pgn_lines:
            if re.search(start, line):
                pgn_games.append(line.strip())
    finally:
        if len(pgn_games):
            return pgn_games
    return


def write_file(path_file, chess_games_write):
    with open(path_file, 'w') as fo:
        for line in chess_games_write:
            fo.write(line + '\n')
            # fo.write('\n')

