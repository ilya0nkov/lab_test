class MyLibrary:

    def __init__(self, n, a, b, c, array):
        self.n = n
        self.a = a
        self.b = b
        self.c = c
        self.array = array

    @staticmethod
    def fibonacci(n):
        if n in (1, 2):
            return 1
        return MyLibrary.fibonacci(n - 1) + MyLibrary.fibonacci(n - 2)

    @staticmethod
    def fibonacci_count(n):
        result = []
        for i in range(1, n + 1):
            result.append(MyLibrary.fibonacci(i))
        return result

    @staticmethod
    def calculate(a, b, c):
        if c == "+":
            return a + b
        if c == "-":
            return a - b
        if c == "*":
            return a * b
        if c == "/":
            return a / b

    @staticmethod
    def bubble_sort(array):
        n = len(array)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swapped = True
            if not swapped:
                break
        return array


if __name__ == "__main__":
    print(MyLibrary.fibonacci_count(10))
    array = [1, 3, 5, 7, 0, 2]
    print(MyLibrary.bubble_sort(array))
