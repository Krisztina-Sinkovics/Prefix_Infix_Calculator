from infix import evaluate_infix_notation
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("( 1 + 2 )", 3),
    ("( 1 + ( 2 * 3 ) )", 7),
    ("( ( 1 * 2 ) + 3 )", 5),
    ("( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )", -1.8),
    ("( 10 - ( 2 * 12 ) )", -14),
    ("( ( 5 + 4 ) - ( 2 * 0 ) )", 9)
])
def test_evaluate_infix_notation(test_input, expected):
    assert eval(test_input) == expected


def test_zero_division():
    assert evaluate_infix_notation("( 15 / ( 1 - 1 ) )") == "You can't divide by zero!"

