# In The Name Of God
# ========================================
# [] File Name : m-fibonacci.py
#
# [] Creation Date : 05-08-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
memory = {}


def m_fibonacci(n):
    if n == 1 or n == 0:
        return 1
    if n in memory:
        return memory[n]
    memory[n] = m_fibonacci(n - 1) + m_fibonacci(n - 2)
    return memory[n]

print(m_fibonacci(10))
