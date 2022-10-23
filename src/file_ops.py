"""
This is a re-write of the project on branch bacon et. al.
bacon is NOT to be merged with main or any other branch
DO NOT MERGE
"""


def read_file(path_file: str):
    pgn_games = []
    try:
        with open(path_file, 'r') as fo:
            pgn_lines = fo.readlines()
    except FileNotFoundError as fnfe:
        print(fnfe)
    else:
        for line in pgn_lines:
            if line.startswith('1.'):
                pgn_games.append(line.strip())
    finally:
        if len(pgn_games):
            return pgn_games
        [print(game) for game in pgn_games]


def write_file(path_file: str, chess_games_write):
    with open(path_file, 'w') as fo:
        for line in chess_games:
            fo.write(line)
            fo.write('\n')


if __name__ == '__main__':
    # read_file('/home/bumper/chess/pgn-one.pgn')
    chess_games = read_file('/home/bumper/chess/games1.pgn')
    write_file('/home/bumper/python/chess_regex/src/test_games.pgn', chess_games)

