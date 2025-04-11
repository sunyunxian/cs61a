"""
high order functions
"""

from operator import add
from typing import Callable


def apply_twice(f: Callable, x):
    return f(f(x))


def square(x):
    return x * x


print(apply_twice(square, 2))


def repeat(f, x):
    while f(x) != x:
        x = f(x)
    return x


def g(y):
    return (y + 5) // 3


"""
1 g(5) = 3 != 5 x = 3
2 g(3) = 2 != 3 x = 2
3 g(2) = 2 == 2 x = 2
4 return x = 2
"""
print(repeat(g, 5))


def make_adder(n):
    def adder(k):
        return k + n

    return adder


add_three = make_adder(3)
print(add_three(4))
print(add_three(5))


def f(x, y):
    return g(x)


def g(a):
    return a + y  # NameError: name 'y' is not defined


try:
    result = f(1, 2)
except NameError as e:
    print(e)


def tripe(x):
    return 3 * x


def compose1(f, g):
    def h(x):
        return f(g(x))

    return h


squiple = compose1(square, tripe)
print(squiple(5))

tripare = compose1(tripe, square)
print(tripare(5))

print(compose1(square, make_adder(2))(3))
"""
compose(square, adder)(3)
h(3)
square(adder(3))
square(5)
25
"""

x = 10
square = x * x  # type: ignore
print(square)

square = lambda x: x * x
print(square(10))

print((lambda x: x * x)(10))

"""
self-reference
"""


def print_all(x):
    print(x)
    return print_all


print_all(10)(10)(10)


def print_sum(x):
    print(x)

    def next_sum(y):
        return print_sum(x + y)

    return next_sum


print_sum(1)(3)(5)
print(print_sum(1)(3)(5))  # <function print_sum.<locals>.next_sum at 0x10093c7c0>


def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)

        return h

    return g


print(add(2, 3))  # 需要 2 个参数
print(curry2(add)(2)(3))  # 需要 1 个参数
