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
            [print(game) for game in pgn_games]


if __name__ == '__main__':
    # read_file('/home/bumper/chess/pgn-one.pgn')
    read_file('/home/bumper/chess/bumper.pgn')

