"""
Iteration
"""

from math import pi, sqrt
from typing import Callable

# Fibonacci sequence
# 参数n是索引的意思


def fib(n):
    """n >= 1，n 是长度，fib 是从 0 开始按照索引计算，也就是传入索引 5 ，计算的是第 6 个值"""
    pred, curr = 0, 1
    k = 1
    while k < n:
        pred, curr = curr, pred + curr
        k += 1
    return curr


for i in range(5):
    print(fib(i), end=" ")
print()


def fib1(n):
    """N >= 0，n 是长度，而计算的时候使用的是索引，可以计算出索引是 0 的值"""
    pred, curr = 1, 0
    k = 0
    while k < n:
        pred, curr = curr, pred + curr
        k += 1
    return curr


for i in range(5):
    print(fib1(i), end=" ")
print()


"""
Designing functions
"""

"""
Higher-Order functions
"""


# 提取出一个 area 函数，非常有效的抽象了各个计算面积的函数
def area(r, shape_constant):
    assert r > 0, "must r > 0"
    return r * r * shape_constant


def area_square(r):
    # return r * r
    return area(r, 1)


def area_circle(r):
    # return r * r * pi
    return area(r, pi)


def area_hexagon(r):
    # return r * r * 3 * sqrt(3) / 2
    return area(r, 3 * sqrt(3) / 2)


# 正常的计算，分别写 2 个函数计算
# 问题是有很多重复的地方，不符合 DRY 原则
def sum_natures(n):
    """
    >>> sum_natures(5)
    15
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1

    return total


def sum_cubes(n):
    """
    >>> sum_cubes(5)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1

    return total


# 抽象后的计算，课程里用的是泛化，generalize
# 把上面 DRY 抽象出来，使用不同的函数实现
def identity(k):
    return k


def cube(k):
    return pow(k, 3)


def summation(n, term):
    """
    >>> summation(5, identity)
    15
    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1

    return total


"""
函数作为返回值
"""


def make_adder(n):
    """
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """

    def adder(k):
        return k + n

    return adder


print(make_adder(1)(2))

"""
lambda expression
"""

x = 10
square = x * x
print(square)

square = lambda x: x * x  # noqa: E731
res = square(10)
print(res)

print((lambda x: x * x)(10))

"""
return
"""


def end(n, d):
    """
    >>> end(34567, 5)
    7
    6
    5
    """
    while n > 0:
        # print(n % 10)
        # n = n // 10 # 对比下面的写法
        last, n = n % 10, n // 10
        print(last)
        if last == d:
            return None


# f是一个函数，
def search(f: Callable[[int], bool]) -> int:
    x = 0
    while True:
        if f(x):
            return x
        x += 1


def is_three(x: int) -> bool:
    return x == 3


print(search(is_three))


def square(x):
    return x * x


def positive(x):
    return max(0, square(x) - 100)


print(positive(2))
print(positive(10))
print(positive(11))


def inverse(f):
    return lambda y: search(lambda x: f(x) == y)


"""
Control
"""


# 解释了为什么没有 real_sqrt 的返回语法
def if_(a, b, c):
    if a:
        return b
    else:
        return c


def real_sqrt(x):
    return if_(x > 0, sqrt(x), 0)


print(real_sqrt(4))
try:
    print(real_sqrt(-1))  # sqrt(-4) 是 ValueError
except ValueError as e:
    print(e)

"""
Control expressions

logical operator
"""


def has_big_sqrt(x):
    return x > 0 and sqrt(x) > 10


print(has_big_sqrt(1))
print(has_big_sqrt(1000))
print(has_big_sqrt(-1000))
