def memo(f):
    memory = {}

    def _f(n):
        print(memory)
        if n in memory:
            print('%d was found' % n)
            return memory[n]
        memory[n] = f(n)
        return memory[n]

    return _f


@memo
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(5))
