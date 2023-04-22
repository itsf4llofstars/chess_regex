#!/usr/bin/bash

cd "$HOME"/python/chess_regex || exit

clear
python3 -m unittest discover -v

exit 0
