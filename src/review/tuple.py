# In The Name Of God
# ========================================
# [] File Name : tuple.py
#
# [] Creation Date : 05-08-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================


t1 = 1, 3, 7, 3
t2 = (1, 3, 7, 2)

data = dict()
data[t1] = 'me'
data[t2] = 'who'

import pprint

pprint.pprint(data)
