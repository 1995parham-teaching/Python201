# In The Name Of God
# ========================================
# [] File Name : list.py
#
# [] Creation Date : 05-08-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================


items = list(range(10))
primes = [2, 3, 5, 7]

print([item for item in items])
print([item for item in items if item not in primes])
print([item * 2 for item in items if item not in primes])
