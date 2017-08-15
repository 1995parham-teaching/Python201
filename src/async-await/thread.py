# In The Name Of God
# ========================================
# [] File Name : thread.py
#
# [] Creation Date : 15-08-2017
#
# [] Created By : Parham Alvani <parham.alvani@gmail.com>
# =======================================
import threading
import time


def run():
    time.sleep(1)
    print("1s elapsed")


threading.Thread(target=run).start()
print("New thread is created")
