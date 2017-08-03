# In The Name Of God
# ========================================
# [] File Name : fibonacci.py
#
# [] Creation Date : 04-08-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================


def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(10))
