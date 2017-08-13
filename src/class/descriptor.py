# In The Name Of God
# ========================================
# [] File Name : descriptor.py
#
# [] Creation Date : 13-08-2017
#
# [] Created By : Parham Alvani <parham.alvani@gmail.com>
# =======================================


class RevealAccess:
    '''
    A data descriptor that sets and returns values
    normally and prints a message logging their access.
    '''

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, instance, owner):
        print('Retrieving', self.name, instance, owner)
        return self.val

    def __set__(self, instance, val):
        print('Updating', self.name, instance, val)
        self.val = val

    def __set_name__(self, owner, name):
        print('Set name', name, owner)


class OutClass:
    x = RevealAccess(10, 'var "x"')
    y = 2


class InClass:
    def __init__(self):
        self.p = RevealAccess(10, 'var "p"')


m = OutClass()

print(m.x)
print(m.y)

m.x = 2

print("###")

n = InClass()

print(n.p)

n.p = 10
