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

curry3 = lambda f: lambda x: lambda y: f(x, y)  # noqa
print(curry3(add)(2)(3))


"""
Q&A
"""


def f(n):
    def g(k):
        return k + n

    return g


foo = f(1)
print(foo(2))
print(foo(3))


def print_sums(n):
    print(n)

    def f(k):
        return print_sum(n + k)

    return f


g = print_sums(1)
h = g(3)
w = h(5)


def f(x):
    me = 1

    def g(y):
        return me  # 这里是嵌套函数的返回值，并不是 f(x) 的结束，而是调用 g(7) 的结束

    me = 2
    print(g(7))
    return x + y


y = 1
z = f(2)  # 打印 2 返回 3 不打印，并不是 g(7) 调用后就返回了


def coffee(grounds):
    x = 4
    return grounds(x)


x = 6
f = lambda x: x + 10
print(coffee(f))  # 14

# 记住，只要是绑定函数，是没有执行的就不会创建 local frame
# 而一旦执行函数（包括 lambda 函数）都会创建 local frame
