# Chess Regex Functions

## Synopsis

This repository is for the Python3 files used to parse chess *.pgn files. It is a set<br>
of functions that can be used to extract single, leagal games from a *.pgn chess file.<br>

The Functions will be able to parse chess games based on certain criteria.<br>

- Only gmaes. Those that start with 1. [a-h][3-4] or N[acfh]3
- Games with no more than n-moves
- Games that end in a draw
- Games that White or Black win
- Games that White or Black win by checkmate
- Games that have no side-lines "(14. Nxf6 Bb2+)"
- Games that have no annotation "{ kibitzing move }"

## PGN File Structure

As of now, the pgn file is required to be in a specific configuration.<br>

```
[Chess Game Meta Data]<br>
[Chess Game Meta Data]<br>
[Chess Game Meta Data]<br>
[Chess Game Meta Data]<br>

1. e4 e5 2. Nf3 Nc6 3. Bb4 a6 4. ... 25. Rxd8# 1-0
```

This is data for a single game. Note that the games moves are on one non-wrapped<br>
line and that the moves are a single space from the each other and from the move
number.<br>
