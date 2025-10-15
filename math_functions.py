def sqrt_newton(x, tolerance=1e-10):
    if x < 0:
        raise ValueError("Cannot compute square root of negative number.")
    guess = x
    while abs(guess * guess - x) > tolerance:
        guess = (guess + x / guess) / 2
    return guess

if __name__ == "__main__":
    val = 25
    print(f"Square root of {val} is approximately {sqrt_newton(val)}")
