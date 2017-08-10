a = 10


def f():
    global a
    print(a)
    a += 1
    print(a)


f()
