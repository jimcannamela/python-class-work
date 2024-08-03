import pytest
import operator
import calculation

@pytest.mark.parametrize("operator, op1, op2, expected", [
    (operator.add, 1, 0, 1),
    (operator.add, -100, 90, -10),
    (operator.add, 1.33333, 5.3, 6.63333),
    (operator.add, '7', 0, 'undefined'),
    (operator.sub, -100, -10, -90),
    (operator.sub, 8, 4, 4),
    (operator.sub, 8.00, 4, 4),
    (operator.mul, -5, -5, 25),
    (operator.mul, 0, 0, 0),
    (operator.truediv, 1, 0, 'undefined'),
    (operator.truediv, 0, 1, 0),
    (operator.mod, -1, 8, 7),
    (operator.mod, 7, 0, 'undefined'),
])
def test_transactions(operator, op1, op2, expected):
    assert calculation.perform_calculation(operator, op1, op2) == expected