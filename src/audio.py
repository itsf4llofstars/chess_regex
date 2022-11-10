"""Initial Python file to play the chess move audio
"""
import subprocess
from time import sleep


def play(mp3: str, secs: float = 0.5) -> None:
    """DOC
    """
    sound = '../audio/' + mp3 + '.mp3'
    subprocess.Popen(['cvlc', sound])
    sleep(secs)


if __name__ == '__main__':
    audio_dict= {
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        'a': 'a',
        'b': 'b',
        'c': 'c',
        'd': 'd',
        'e': 'e',
        'f': 'f',
        'g': 'g',
        'h': 'h',
        'R': 'rook',
        'N': 'knight',
        'B': 'bishop',
        'Q': 'queen',
        'K': 'king',
        '=': 'promote',
        'O': 'castle',
        ' ': ' ',
        'x': 'takes',
    }

    test_game = ['1. e4 e5 2. Nf3 Nc6 3. Bxc6 fxg1=Q']
    test_str = ''.join(test_game)
    print(test_str)

    index = 0
    while index < len(test_str):
        if test_str[index] == '.':
            index += 1
            continue

        print(audio_dict[test_str[index]])
        index += 1

