#!/usr/bin/env python3
import os
import re


def check_path_format(path, filename):
    if not path.startswith('/'):
        path = '/' + path
    return path


if __name__ == "__main__":
    file_path = "home/bumper/python/chess_regex"
    file_path = check_path_format(file_path, 'nnn')
    print(file_path)
