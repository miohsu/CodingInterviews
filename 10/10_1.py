"""
    求斐波那契数列的第n项
"""


def fibonacci(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        n += 1
        a, b = b, a + b


if __name__ == '__main__':
    res = fibonacci(10)
    print(list(res))
