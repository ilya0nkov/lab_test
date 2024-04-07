import pytest
from library import MyLibrary

@pytest.mark.parametrize("n, expected_result", [
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55)
])
def test_fibonacci(n, expected_result):
    actual_result = MyLibrary.fibonacci(n)
    assert actual_result == expected_result

@pytest.mark.parametrize("n, expected_result", [
    (10, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]),
    (5, [1, 1, 2, 3, 5]),
    (0, []),
    (1, [1])
])
def test_fibonacci_count(n, expected_result):
    actual_result = MyLibrary.fibonacci_count(n)
    assert actual_result == expected_result

@pytest.mark.parametrize("a, b, action, expected_result", [
    (3, 2, "+", 5),
    (5, 3, "-", 2),
    (4, 2, "*", 8),
    (6, 4, "/", 1.5)
])
def test_calculate(a, b, action, expected_result):
    actual_result = MyLibrary.calculate(a, b, action)
    assert actual_result == expected_result

@pytest.mark.parametrize("input_value, expected_result", [
    ([1, 3, 5, 7, 0, 2], [0, 1, 2, 3, 5, 7]),
    ([], []),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])
])
def test_bubble_sort(input_value, expected_result):
    actual_result = MyLibrary.bubble_sort(input_value)
    assert actual_result == expected_result
