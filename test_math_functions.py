from math_functions import sqrt_newton

def test_sqrt_newton():
    assert abs(sqrt_newton(25) - 5) < 1e-7
    assert abs(sqrt_newton(0) - 0) < 1e-7
