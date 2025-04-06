"""
CS61A 2020因为疫情的原因，所以很多都是在线的课程，包括 Q&A

学习的时候可以从 2020 年开始的视频为主，同时点开最新的课程主页，看一下 lecture 的 video 链接，如果有最新的可以同时看
"""

################################
# Lecture3
################################
from operator import add, floordiv, mod, mul, truediv

print(1)
print(print(1), print(2))
"""
1
2
None None
"""


def does_not_square(x):
    x * x  # type: ignore


does_not_square(4)
sixteen = does_not_square(4)
try:
    sixteen + 4  # type: ignore
except TypeError as e:
    print(e)


def square(x):
    return mul(x, x)


res = square(square(3))
print(res)

# 2 + 3 * 4 +5 转换为操作符的写法
print(add(add(2, mul(3, 4)), 5))

# (2 + 3) * (4 + 5) 转换为操作符的写法
print(mul(add(2, 3), add(4, 5)))

print(2013 / 10, truediv(2013, 10))
print(2013 // 10, floordiv(2013, 10))

print(2013 % 10, mod(2013, 10))


# 多个返回值
def divide_exact(n, d):
    """Return the quotient and remainder of dividing N by D
    >>> q, r = divide_exact(2013, 10)
    >>> q
    201
    >>> r
    3
    """
    return n // d, n % d


# 多个赋值表达式在 1 行
quotient, remainder = divide_exact(2013, 10)
print(quotient, remainder)

# 如果不想在 source file 有太多的 print，可以调用解释器模式
# python -i <source file name>.py

# doctest 模式，可以用 python -m doctest -v <source file name>.py 执行函数的测试文档
# -v 表示输出测试的信息

# condition statement


def absolute_value(x):
    """Return the absolute value
    >>> x = absolute_value(1)
    >>> x
    1
    >>> x = absolute_value(-1)
    >>> x
    1
    >>> x = absolute_value(0)
    >>> x
    0
    """
    if x > 0:
        return x
    elif x == 0:
        return 0
    else:
        return -x


i, total = 0, 0

while i < 3:
    i = i + 1
    total = total + i

print(f"i = {i}, total = {total}")


def prime_factors(n):
    """Print the prime factors of n
    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(9)
    3
    3
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(11)
    11
    >>> prime_factors(12)
    2
    2
    3
    >>> prime_factors(858)
    2
    3
    11
    13
    """
    while n > 1:
        k = smallest_prime_factor(n)
        n = n // k
        print(k)


def smallest_prime_factor(n):
    """Return the smallest k > 1 that evenly divides n.
    >>> x = smallest_prime_factor(2)
    >>> x
    2
    >>> x = smallest_prime_factor(3)
    >>> x
    3
    >>> x = smallest_prime_factor(10)
    >>> x
    2
    """
    k = 2
    while n % k != 0:
        k = k + 1
    return k


prime_factors(858)

################################
# Q&A
################################


def g(z):
    return z + 3


def f(x):
    y = g(x + 1)
    return y + 7


print(f(1))

x = 2


def f():
    try:
        print(x)  # type: ignore
    except UnboundLocalError as e:
        print(e)
    x = 3
    print(x)


f()

x = 2


def f():
    global x
    print(x)
    x = 3
    print(x)


f()

x = 2


def f():
    print(x)


f()
print(5 / 2)  # 2.5
print(5 // 2)  # 2
print(-5 // 2)  # -3
print(round(5 / 2))  # 2
print(round(5 // 2))  # 2

# round 在处理整数中间值的时候，会舍入到最近的偶数,仅限于 .5，而不是涉及多个位数
# 如果想要更加精确的值，不要用 round
print(round(2.5))  # 2
print(round(2.51))  # 3
print(round(3.5))  # 4

# python 中真价值问题

if -12:
    print("-12 is true")
