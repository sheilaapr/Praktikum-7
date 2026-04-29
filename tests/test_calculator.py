from calculator import add, divide

def test_add_basic():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide_basic():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    try:
        divide(1, 0)
        assert False, "Expected ValueError"
    except ValueError:
        pass
