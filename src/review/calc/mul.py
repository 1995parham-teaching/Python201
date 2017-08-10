def mul(*args):
    mul = 1
    for i in args:
        mul *= i
    return mul


if __name__ == '__main__':
    r = mul(1, 2, 3, 4)
    if r == 24:
        print('S')
    else:
        print('F')
