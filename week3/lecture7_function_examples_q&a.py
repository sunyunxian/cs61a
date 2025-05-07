def likes(n):
    """"""
    pass


def mystery1(n):
    k = 1
    while k < n:
        if likes(n):
            print(k)
        k = k + 2


def flip(flop):
    if flop > 2:
        return None
    flip = lambda flip: 3  # noqa
    return flip


def flop(flip):

    return flop


# flip, flop = flop, flip

# flip(flop(1)(2))(3)


def trace1(fn):
    """Returns a version of fn that first print
    fn -a function of 1 argument
    """

    def traced(x):
        print("Calling", fn, "on argument", x)
        return fn(x)

    return traced


# @trace1
def square(x):

    return x * x


@trace1
def sum_squares_up_to(n):

    k = 1
    total = 0
    while k <= n:
        total = total + square(k)
        k = k + 1
    return total


square(12)
trace1(square)(12)
# sum_squares_up_to(5)


# def repeat(k):
#     """When called repeatedly, print each repeated argument.
#     >>> f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
#     7
#     1
#     5
#     1
#     """

#     return --(k)

# def detector(r):

#     def g(i):
#         if --:
#             --
#             return

#     return g

foo = lambda j: j == 7  # noqa

print(foo(10))
