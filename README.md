# Chess Regex Functions

Note: Most of this text are notes to the author and or colaborators. It is not meant
to be readable by a user.

**Please Note:** Although not much is going on with this project it is currently for use
with the Linux operating system. I have not yet begun to understand how to make this cross
platform for Windows or Mac. I do apologize.

## Synopsis

This repository is for the Python3 files used to parse chess *.pgn files. It is a set
of functions that can be used to extract single, legal games from a*.pgn chess file.
I have since grown the project into a chess audio study, this repo will most likely be
deleted in lue of the audio project.

The Functions will be able to parse chess games based on certain criteria.

- Only gmaes. Those that start with legal chess moves
- Games with no more than n-moves user selects n
- Games with at least 10 moves
- Games with no more than 99 moves
- Games that end in a draw
- Games that White or Black win
- Games that White or Black win by checkmate
- Games that have no side-lines "(14. Nxf6 Bb2+)"
- Games that have no annotation "{ kibitzing move }"

## PGN File Structure

As of now, the pgn file is required to be in a specific configuration.

```text
[Chess Game 1 Meta Data]
[Chess Game 1 Meta Data]
[Chess Game 1 Meta Data]
[Chess Game 1 Meta Data]

1. e4 e5 2. Nf3 Nc6 3. Bb4 a6 4. + ... + 25. Rxd8# 1-0

[Chess Game 2 Meta Data]
[Chess Game 2 Meta Data]
[Chess Game 2 Meta Data]
[Chess Game 2 Meta Data]

1. e4 e5 2. Nf3 Nc6 3. Bb4 a6 4. + ... + 25. Rxd8# 1-0

+
.
.
.
+

[Chess Game n Meta Data]
[Chess Game n Meta Data]
[Chess Game n Meta Data]
[Chess Game n Meta Data]

1. e4 e5 2. Nf3 Nc6 3. Bb4 a6 4. + ... + 25. Rxd8# 1-0
```

This is data for a single game. Note that the games moves are on one non-wrapped
line and the move numbers are a single space from the piece move nomenclature.

## Project Updates

Individuale functions for parsing have been written and tested. Along with these a
single functions file big_parser.py has been written that does all the parsing in one
function. A one function file is usefull for memory pruposes when parsing large (100 million)
chess games pgn files.
