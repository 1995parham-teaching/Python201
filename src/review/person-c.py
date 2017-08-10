class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print("Hello %s" % self.name)


class Runner(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


r = Runner('Parham', 20)
r.say()
Runner.say(r)
print(r.name)
