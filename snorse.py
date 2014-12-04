from __future__ import unicode_literals

import os

import click


DOT = "\u2603"
DASH = "\u26C4\u26C4\u26C4"


MORSE = {
    'a': (DOT, DASH),
    'b': (DASH, DOT, DOT, DOT),
    'c': (DASH, DOT, DASH, DOT),
    'd': (DASH, DOT, DOT),
    'e': (DOT,),
    'f': (DOT, DOT, DASH, DOT),
    'g': (DASH, DASH, DOT),
    'h': (DOT, DOT, DOT, DOT),
    'i': (DOT, DOT),
    'j': (DOT, DASH, DASH, DASH),
    'k': (DASH, DOT, DASH),
    'l': (DOT, DASH, DOT, DOT),
    'm': (DASH, DASH),
    'n': (DASH, DOT),
    'o': (DASH, DASH, DASH),
    'p': (DOT, DASH, DASH, DOT),
    'q': (DASH, DASH, DOT, DASH),
    'r': (DOT, DASH, DOT),
    's': (DOT, DOT, DOT),
    't': (DASH,),
    'u': (DOT, DOT, DASH),
    'v': (DOT, DOT, DOT, DASH),
    'w': (DOT, DASH, DASH),
    'x': (DASH, DOT, DOT, DASH),
    'y': (DASH, DOT, DASH, DASH),
    'z': (DASH, DASH, DOT, DOT),
    '1': (DOT, DASH, DASH, DASH, DASH),
    '2': (DOT, DOT, DASH, DASH, DASH),
    '3': (DOT, DOT, DOT, DASH, DASH),
    '4': (DOT, DOT, DOT, DOT, DASH),
    '5': (DOT, DOT, DOT, DOT, DOT),
    '6': (DASH, DOT, DOT, DOT, DOT),
    '7': (DASH, DASH, DOT, DOT, DOT),
    '8': (DASH, DASH, DASH, DOT, DOT),
    '9': (DASH, DASH, DASH, DASH, DOT),
    '0': (DASH, DASH, DASH, DASH, DASH),
}

UNMORSE = dict(
    (v, k) for k, v in MORSE.items()
)


LETTER_SPACING = '   '
CHARACTER_SPACING = ' '
WORD_SPACING = '       '


def word_to_morse(word):
    return LETTER_SPACING.join(map(
        lambda c: CHARACTER_SPACING.join(MORSE.get(c.lower(), [c])),
        word,
    ))


def snorse(text):
    words = filter(bool, text.split(' '))
    return WORD_SPACING.join(map(
        word_to_morse,
        words,
    ))


def morse_to_word(morse):
    letters = morse.split(LETTER_SPACING)
    return ''.join(map(
        lambda c: UNMORSE.get(tuple(c.split(CHARACTER_SPACING)), c),
        letters,
    ))


def desnorse(text):
    words = filter(bool, text.split(WORD_SPACING))
    return ' '.join(map(
        morse_to_word,
        words,
    ))


@click.command()
@click.argument('text', required=False)
@click.option('-f', '--file', type=click.File())
def snorse_cli(text=None, file=None):
    if file is not None:
        text = file.read()
    elif text is None:
        text = click.get_text_stream('stdin').read()
    elif os.path.exists(os.path.expanduser(text)):
        text = open(os.path.expanduser(text)).read()
    click.echo(snorse(text))


@click.command()
@click.argument('text', required=False)
@click.option('-f', '--file', type=click.File())
def desnorse_cli(text=None, file=None):
    if file is not None:
        text = file.read()
    elif text is None:
        text = click.get_text_stream('stdin').read()
    elif os.path.exists(os.path.expanduser(text)):
        text = open(os.path.expanduser(text)).read()
    click.echo(desnorse(text))
