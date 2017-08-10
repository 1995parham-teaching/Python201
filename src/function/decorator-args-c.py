def decorator_args(is_wrap):
    def decorator(f):
        print("decorator called")

        def _f(*args, **kwargs):
            print("before")
            f(*args, **kwargs)
            print("after")

        if is_wrap is True:
            return _f
        else:
            return f
    return decorator


@decorator_args(True)
def hello():
    print("Hello")


hello()
