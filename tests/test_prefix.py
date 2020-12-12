from prefix import evaluate_prefix_notation
import pytest


def test_single_number():
    assert evaluate_prefix_notation("3") == 3


def test_addition():
    assert evaluate_prefix_notation("+ 1 2") == 3


def test_difference():
    assert evaluate_prefix_notation("- 0 3") == -3


def test_division():
    assert evaluate_prefix_notation("/ 3 2") == 1.5


def test_longer_expression():
    assert evaluate_prefix_notation("+ 1 * 2 3") == 7


def test_longer_expression_without_operator_separation():
    assert evaluate_prefix_notation("+ * 1 2 3") == 5


def test_all_four_operands():
    assert evaluate_prefix_notation("- / 10 + 1 1 * 1 2") == 3


def test_zero_division():
    assert evaluate_prefix_notation("/ 3 0") == "You can't divide by zero!"
