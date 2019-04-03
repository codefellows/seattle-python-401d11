from .misc import has_dupes, most_common_word, calculate, each_item
import pytest

def test_dupes():

    assert has_dupes('abba')

    assert not has_dupes('abc')

def test_most_common_word():
    assert most_common_word('an apple an apple apple') == 'apple'


def test_calculate():
    assert calculate('add',3,4) == 7



        