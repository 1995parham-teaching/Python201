import functools


def accept_all(*args, **kwargs):
    print(args, kwargs)


def sum(*args):
    s = functools.reduce(lambda x, y: x + y, args)
    print(s)


def g(**kwargs):
    print(kwargs)


sum(1, 2, 3, 4)
sum(*[1, 2, 3, 4, 5])
g(a=1, b=2, c=3)
accept_all(1, 2, 3)
accept_all(2, b=1)


def w(a, b, c):
    print(a + b + c)


l = [1, 2, 3]
w(l[0], l[1], l[2])
w(*l)
