import SevenWonders
import pytest
def test_red_score():
    r = SevenWonders.conquest_score
    assert r.red_score() == 2

# def inc(x):
#     return x+1
# def test_example():
#     assert inc(3) == 5