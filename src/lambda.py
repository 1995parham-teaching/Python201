def r(f, l):
    for i in l:
        print(f(i))


r(lambda x: x + 10, [1, 2, 3])
