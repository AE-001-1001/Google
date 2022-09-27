import pytest

def inc(x):
    return x+1

def deg(y):
    pytest.console_main()
    return y-1

def test_answer():
    assert inc(3) == 3+1
    return 0

def test_answr2():
    assert deg(2) == 2-1
    return 0

def test_main():
    test_answer()
    test_answr2()
    return 0
    
test_main()