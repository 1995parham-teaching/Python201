import functools

foo = [1, 2, 3]
functools.reduce(lambda x, y: x + y, foo)


def r(f, l):
    for i in l:
        print(f(i))


r(lambda x: x + 10, [1, 2, 3])
