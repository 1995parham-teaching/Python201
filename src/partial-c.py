def partial(f, *args):
    default = args

    def _f(*args, **kwargs):
        f(*default, *args, **kwargs)

    return _f


def say(name, message):
    print("%s: %s" % (name, message))


new_say = partial(say, 'parham')
new_say('Hello')
new_say('Hello', 123)
