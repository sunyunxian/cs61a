def welcome():
    print("Go")
    return "hello"


def cal():
    print("Bears")
    return "world"


welcome()
"""
Go
"""
print(welcome(), cal())
"""
Go
Bears
hello world
"""


def ab(c, d):
    if c > 5:
        print(c)
    elif c > 7:
        print(d)
    print("foo")


ab(10, 20)
"""
10
foo
"""


def bake(cake, make):
    if cake == 0:
        cake = cake + 1
        print(cake)
    if cake == 1:
        print(make)
    else:
        return cake
    return make


bake(0, 29)
"""
1
29
29 # 这里是解释器里面的返回，所以会打印的
"""
bake(1, "mashed potatoes")
"""
mashed potatoes
mashed potatoes
"""
