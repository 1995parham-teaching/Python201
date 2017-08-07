# In The Name Of God
# ========================================
# [] File Name : decorator-args.py
#
# [] Creation Date : 07-08-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import functools


def decorator_args(arg1, arg2):
    def decorator(f):
        @functools.wraps(f)
        def wrapper():
            print(arg1)
            f()
            print(arg2)
        return wrapper
    return decorator


@decorator_args('before', 'after')
def hello():
    print('Hi')


hello()
