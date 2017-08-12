# In The Name Of God
# ========================================
# [] File Name : bool.py
#
# [] Creation Date : 12-08-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================


class IsBool:
    def __init__(self, age):
        self.age = age

    def __bool__(self):
        return self.age > 20


is_bool = IsBool(23)

if bool(is_bool) is True:
    print("is_bool.age > 20")
else:
    print("is_bool.age <= 20")

if is_bool:
    print("is_bool.age > 20")
else:
    print("is_bool.age <= 20")

print(bool(is_bool))
