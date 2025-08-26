from core.dice import Dice

def test_roll_returns_list():
    r = Dice().roll()
    assert isinstance(r, list)
    assert all(1 <= x <= 6 for x in r)
    assert len(r) in (2,4)
