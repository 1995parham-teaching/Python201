def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


if __name__ == '__main__':
    r = sum(1, 2, 3, 4)
    if r == 10:
        print('S')
    else:
        print('F')
