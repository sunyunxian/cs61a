a = 1


def f(g):
    a = 2
    return lambda y: a * g(y)


f(lambda y: a + y)(a)
"""

f(lambda y: 1 + y) -> lambda y: 2 * g(y)

(lambda y: 2 * g(y))(1) -> (lambda 1: 2 * g(1))

g(1) -> lambda 1: a + 1 -> lambda 1: 1 + 1 = 2

lambda 1: 2 * 2 = 4

"""


def f(x):
    return g(x)


def g(y):
    return h(y) + y


def h(z):
    return z // z


# f(0)


def end(n, d):
    """
    >>> end(34567, 5)
    7
    6
    5
    """
    while n > 0:
        digit = n % 10
        print(digit)
        if digit == d:
            break
        n = n // 10


def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1


def is_three(x):
    return x == 3


print(search(is_three))


def square(x):
    return x * x


def positive(x):
    return max(0, square(x) - 100)


print(search(positive))
