# In The Name Of God
# ========================================
# [] File Name : generators.py
#
# [] Creation Date : 15-08-2017
#
# [] Created By : Parham Alvani <parham.alvani@gmail.com>
# =======================================


def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1


for i in firstn(10):
    print(i)
