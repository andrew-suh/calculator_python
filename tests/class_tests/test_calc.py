from src.calculator.calc_class import calc_app

#create calculator class
tester = calc_app()

def test_calc_add():
    assert tester.add(1, 2) == 3


def test_calc_sub():
    assert tester.subtract(1, 2) == -1
    assert tester.subtract(2, 1) == 1
    assert tester.subtract(2, 2) == 0


def test_calc_divide():
    assert int(tester.divide(2, 1)) == 2
    assert int(tester.divide(2, 2)) == 1


def test_calc_mul():
    assert tester.multiply(1, 1) == 1
    assert tester.multiply(2, 2) == 4
