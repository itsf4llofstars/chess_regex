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

