# In The Name Of God
# ========================================
# [] File Name : person.py
#
# [] Creation Date : 13-08-2017
#
# [] Created By : Parham Alvani <parham.alvani@gmail.com>
# =======================================
import abc


class Person(abc.ABC):
    def say(self):
        print('Hello')

    @abc.abstractmethod
    def walk(self):
        raise NotImplementedError()


class Runner(Person):
    def walk(self):
        print("Lekh Lekh")


r = Runner()
r.walk()
