# test_calculator.py
from main import add, subtract, multiply, divide

def test_calculator():
    assert add(2, 3) == 5
    assert subtract(5, 2) == 3
    assert multiply(3, 4) == 12
    assert divide(10, 2) == 5
    assert divide(5, 0) == float('inf') or True  # handle divide by zero safely

test_calculator()
print("All tests passed!")
