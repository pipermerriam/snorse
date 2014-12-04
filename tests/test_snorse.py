from __future__ import unicode_literals

import pytest

import snorse


DOT = "\u2603"
DASH = "\u26C4\u26C4\u26C4"
@pytest.mark.parametrize(
    'text,expected',
    (
        ('', ''),
        ('a', '\u2603 \u26C4\u26C4\u26C4'),
        ('abc', '\u2603 \u26C4\u26C4\u26C4   \u26C4\u26C4\u26C4 \u2603 \u2603 \u2603   \u26C4\u26C4\u26C4 \u2603 \u26C4\u26C4\u26C4 \u2603'),
        ('abc abc', '\u2603 \u26C4\u26C4\u26C4   \u26C4\u26C4\u26C4 \u2603 \u2603 \u2603   \u26C4\u26C4\u26C4 \u2603 \u26C4\u26C4\u26C4 \u2603       \u2603 \u26C4\u26C4\u26C4   \u26C4\u26C4\u26C4 \u2603 \u2603 \u2603   \u26C4\u26C4\u26C4 \u2603 \u26C4\u26C4\u26C4 \u2603'),
        ('a b c', '\u2603 \u26C4\u26C4\u26C4       \u26C4\u26C4\u26C4 \u2603 \u2603 \u2603       \u26C4\u26C4\u26C4 \u2603 \u26C4\u26C4\u26C4 \u2603'),
        ('a&', '\u2603 \u26C4\u26C4\u26C4   &'),
    ),
)
def test_conversion(text, expected):
    actual = snorse.snorse(text)
    assert actual == expected
