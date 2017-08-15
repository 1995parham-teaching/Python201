import threading


def foo(m, n):
    for i in range(m, n):
        print('\t%d' % i)


for i in range(10):
    t = threading.Thread(target=foo, args=((i-1) * 10, i * 10))
    t.start()
