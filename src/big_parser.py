# Initial write of big_parser.py the file that parses
# all user selects in one function


def parse_chess(file_name):
    with open(file_name, 'r') as fo:
        for line in fo:
            line = line.strip()
            if not line.startswith('1. ') or '\(' in line:
                continue
