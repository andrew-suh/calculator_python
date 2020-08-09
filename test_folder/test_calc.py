from ..calculator.calc_class import calc_app

def test_calc_add():
    tester = calc_app()
    assert tester.add(1,2) is 3

def test_calc_sub():
    tester = calc_app()
    assert tester.subtract(1,2) is -1
    assert tester.subtract(2,1) is 1
    assert tester.subtract(2,2) is 0

def test_calc_divide():
    tester = calc_app()
    assert int(tester.divide(2,1)) is 2
    assert int(tester.divide(2,2)) is 1

def test_calc_mul():
    tester = calc_app()
    assert tester.multiply(1,1) is 1
    assert tester.multiply(2,2) is 4
