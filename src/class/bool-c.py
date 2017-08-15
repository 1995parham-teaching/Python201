class Hello(object):
    def __init__(self, age):
        self.age = age

    def __bool__(self):
        if self.age > 18:
            return True
        else:
            return False


def check(b):
    if b:
        return True
    else:
        return False


print(check(True))
print(check(1))
print(check(Hello(19)))
print(check(Hello(16)))
