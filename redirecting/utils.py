import os

from random import sample
from pathlib import Path

DIR = Path(os.path.dirname(__file__))

with open(DIR / "words.txt", "r") as file:
    _words = file.readlines()

_words = [word.strip().title() for word in _words]


def gen_tokipona_identifier(words=4) -> str:
    return "".join(sample(_words, words))
