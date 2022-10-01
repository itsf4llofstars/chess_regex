#!/usr/bin/env python3
"""ATTENTION: This branch is the checking branch, it is to be used and deleted without
merging into any other branch
"""
import re

chess_pgn = [
    "[meta data]\n",
    "[meta data]\n",
    "\n",
    "1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 65. O-O Be7 6. Re1# 1-0\n",
    "\n",
    "[meta data]\n",
    "[meta data]\n",
    "\n",
    "1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 Rxf3# 0-1\n",
]

regex = re.compile(r'\s[4-9]\d\.\s')
ans = []
[ans.append(line.strip()) for line in chess_pgn if not re.search(regex, line)]
[print(line) for line in ans]
