# test_calculations.py

from calculs import addition, soustraction, multiplication, coucou

def test_calc_addition():
    assert addition(2, 4) == 6
def test_calc_substraction():
    assert soustraction(2, 4) == -2
def test_calc_multiply():
    assert multiplication(2, 4) == 8
def test_coucou():
    assert coucou() == 'hello'
