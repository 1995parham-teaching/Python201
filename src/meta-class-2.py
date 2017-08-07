# In The Name Of God
# ========================================
# [] File Name : meta-class-2.py
#
# [] Creation Date : 08-08-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================


class ParhamClass(type):

    def __new__(cls, name, bases, namespace, **kwargs):
        print('cls: ', cls)
        print('name: ', name)
        print('bases: ', bases)
        print('namespace: ', namespace)
        print('kwargs: ', kwargs)
        result = super().__new__(cls, name, bases, namespace)

        return result


class A(str, when='never', metaclass=ParhamClass):
    name = 'parham'

    def one(): pass

    def two(): pass

    def three(): pass

    def four(): pass
