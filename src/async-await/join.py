# In The Name Of God
# ========================================
# [] File Name : join.py
#
# [] Creation Date : 15-08-2017
#
# [] Created By : Parham Alvani <parham.alvani@gmail.com>
# =======================================
import threading
import time
hello = 0


def foo():
    global hello
    time.sleep(1)
    hello += 10


t = threading.Thread(target=foo)
t.start()
t.join()
print(hello)
