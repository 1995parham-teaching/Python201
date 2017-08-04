# In The Name Of God
# ========================================
# [] File Name : person.py
#
# [] Creation Date : 04-08-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('%s: Hello' % self.name)

    def walk(self):
        print('Telgh Telgh')


class Runner(Person):
    def __init__(self, name, age):
        super(name, age)

    def walk(self):
        print('Lekh Lekh')
