"""Initial Python file to play the chess move audio
"""
import subprocess
from time import sleep


def get_each_move(chess_game):
    each_move = chess_game.split(' ')
    return each_move


def play(mp3: str, secs: float = 0.5) -> None:
    """Adds together the relative audio path with
    the mp3 file and appends the extensio .mp3.
    Calls the supprocess command to play the single
    audio mp3 file. Requires the audio player call.
    This call is cvlc, vlc, or celluloid at this time.
    The sleep time is the time between audio calls, as
    function waits here to prevent audio overlap.

    args:
        mp3 (str): Name of mp3 file without the extension
        secs (float): Time to sleep till ending the function
    """
    sound = './audio/' + mp3 + '.mp3'
    subprocess.Popen(['cvlc', sound])
    sleep(secs)


if __name__ == '__main__':
    audio_dict = {
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
    opera = ['1. e4 e5 2. Nf3 d6 3. d4 Bg4 4. dxe5 Bxf3 5. Qxf3 dxe5 6. Bc4 Nf6 7. Qb3 Qe7 8. Bg5 c6 9. Nc3 b5 10. Nxb5 cxb5 11. Bxb5+ Nbd7 12. O-O-O Rd8 13. Rxd7 Rxd7 14. Rd1 Qe6 15. Bxd7+ Nxd7 16. Qb8+ Nxb8 17. Rd8#']
    test_str = ''.join(opera)
    print(test_str)

    index = 0
    while index < len(test_str):
        if test_str[index] == '.' or test_str[index] == ' ':
            index += 1
            # sleep(1.0)
            continue

        print(audio_dict[test_str[index]])
        # play(audio_dict[test_str[index]])
        index += 1

