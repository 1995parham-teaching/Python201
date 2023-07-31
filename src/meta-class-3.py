# In The Name Of God
# ========================================
# [] File Name : meta-class.py
#
# [] Creation Date : 05-08-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from typing import List


class BotFather:
    bots: List[type] = []

    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print("New subclass from BotFather")
        BotFather.bots.append(cls)


print(BotFather.bots)


class HelloBot(BotFather):
    name: str = 'hello'

    def __init__(self):
        print("New instance from HelloBot")


print(BotFather.bots)
