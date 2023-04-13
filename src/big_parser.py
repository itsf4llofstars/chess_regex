# Initial write of big_parser.py the file that parses
# all user selects in one function
import os
import random
import re


def parse_games(file_name, max_move, min_move, white, mate):
    games = []
    random_game = ""
    with open(file_name, "r") as fo:
        for line in fo:
            if (
                not line.startswith("1. ")
                or max_move in line
                or min_move not in line
                or not line[-3] == "-"
                or "(" in line
                or ")" in line
                or "{" in line
                or "}" in line
                or "[" in line
                or "]" in line
                or "<" in line
                or ">" in line
            ):
                continue
            else:
                line = line.replace("!", "")
                line = line.replace("?", "")
                line = line.replace("+", "")
                line = line.rstrip()

                if white and mate:
                    if line.endswith(" 1-0") and "#" in line:
                        games.append(line)
                elif white and not mate:
                    if line.endswith(" 1-0") and "#" not in line:
                        games.append(line)
                elif not white and mate:
                    if line.endswith(" 0-1") and "#" in line:
                        games.append(line)
                elif not white and not mate:
                    if line.endswith(" 0-1") and "#" not in line:
                        games.append(line)

    # Second white move not tested
    legal_start = re.compile(
        r"^(1\.\s[a-hN][3-4acfh]3?\s[a-hN][5-6acfh]6?\s2\.\s[a-hBNKQR][1-6a-h])"
    )
    while True:
        random_game = random.choice(games)

        if re.search(legal_start, random_game):
            break

    del games
    return random_game


def main():
    file_name = os.path.expanduser(os.path.join("~", "chess", "bumper.pgn"))
    min_move = " 10. "
    max_move = " 40. "
    white = False
    mate = False

    study_game = parse_games(file_name, max_move, min_move, white, mate)
    print(study_game)


if __name__ == "__main__":
    main()
