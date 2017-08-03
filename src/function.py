# In The Name Of God
# ========================================
# [] File Name : function.py
#
# [] Creation Date : 03-08-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================


def function_name(param1, param2):
    '''
    I am your function documentation but you can use me in other
    maybe bad ways
    '''
    print('You saw me in the past')


print(function_name.__doc__)


def function_bad():
    '''print('Hello from the doc')'''
    pass


print(exec(function_bad.__doc__))
