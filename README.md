# Chess Regex Functions

Note: Most of this text is self notes to the author and or colaborators. It is not meant
to be readable by a user.

**Please Note:** Although not much is going on with this project it is currently for use<br>
with the Linux operating system. I have not yet begun to understand how to make this cross<br>
platform for Windows or Mac. I do apologize.

## Synopsis

This repository is for the Python3 files used to parse chess *.pgn files. It is a set<br>
of functions that can be used to extract single, leagal games from a *.pgn chess file.<br>

The Functions will be able to parse chess games based on certain criteria.<br>

- Only gmaes. Those that start with 1. [a-h][3-4] or N[acfh]3
- Games with no more than n-moves user selects n
- Games with no more than 99 moves
- Games that end in a draw
- Games that White or Black win
- Games that White or Black win by checkmate
- Games that have no side-lines "(14. Nxf6 Bb2+)"
- Games that have no annotation "{ kibitzing move }"

## PGN File Structure

As of now, the pgn file is required to be in a specific configuration.<br>

```
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

This is data for a single game. Note that the games moves are on one non-wrapped<br>
line and the move numbers are a single space from the piece move nomenclature.<br>

## Project Updates

A seperate non-pushed, non-merged branch has been finallized to the extent of the code<br>
being able to parse pgn files. Work now back on the project proped is to continue with<br>
parsing the pgn file and extracting the requested games.<br>

