import pytest
from library import MyLibrary


class TestLibraryMethods:

    def test_fibonacci(self):
        expected_result = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

        actual_results = []
        for i in range(1, 11):
            result = MyLibrary.fibonacci(i)
            actual_results.append(result)

        assert actual_results == expected_result

    def test_fibonacci_count(self):
        expected_result = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

        len_real_result = len(expected_result)
        actual_result = MyLibrary.fibonacci_count(len_real_result)

        assert actual_result == expected_result

    def test_calculate(self):
        expected_result = [5, 1, 6, 1.5]
        input_values = [3, 2]
        actions = ["+", "-", "*", "/"]

        actual_results = []
        for i in range(len(actions)):
            result = MyLibrary.calculate(input_values[0], input_values[1], actions[i])
            actual_results.append(result)

        assert actual_results == expected_result

    def test_bubble_sort(self):
        expected_result = [0, 1, 2, 3, 5, 7]
        input_value = [1, 3, 5, 7, 0, 2]

        actual_result = MyLibrary.bubble_sort(input_value)

        assert actual_result == expected_result
