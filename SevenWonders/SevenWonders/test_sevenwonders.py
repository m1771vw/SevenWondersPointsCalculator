from SevenWonders import conquest_score
def test_red_score():
    r = conquest_score
    assert r.red_score() == 2

def inc(x):
    return x+1
def test_example():
    assert inc(3) == 5