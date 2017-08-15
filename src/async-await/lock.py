# In The Name Of God
# ========================================
# [] File Name : lock.py
#
# [] Creation Date : 15-08-2017
#
# [] Created By : Parham Alvani <parham.alvani@gmail.com>
# =======================================
import threading


l = []
lck = threading.Lock()


def foo():
    with lck:
        while True:
            l.append(1)
            print(l)


def boo():
    with lck:
        while True:
            l.append(2)
            print(l)


threading.Thread(target=foo).start()
threading.Thread(target=boo).start()
