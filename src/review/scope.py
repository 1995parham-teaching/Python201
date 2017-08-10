# In The Name Of God
# ========================================
# [] File Name : scope.py
#
# [] Creation Date : 05-08-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================


def f1():
    a = 1
    b = []

    def f2():
        print(a)
        b.append(1)
    print(b)
    f2()
    print(a)
    print(b)

f1()
