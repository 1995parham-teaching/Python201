# In The Name Of God
# ========================================
# [] File Name : partial.py
#
# [] Creation Date : 05-08-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================


def partial(f, *args):
    param = args

    def _f(*args, **kwargs):
        return f(*param, *args, **kwargs)

    return _f


def say(name, message):
    print(f'{message} to {name}')


say('parham', 'hello')

say_to_parham = partial(say, 'parham')
say_to_parham('bye bye')
