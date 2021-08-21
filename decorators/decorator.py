def decorator(validator):
    def g(func):
        def h(*args, **kwargs):
            if validator(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                return "error"

        return h

    return g


def validator(x):
    return x >= 0


@decorator(validator)
def f(x):
    return x ** 0.5


print(f(4))  # should print 2.0
print(f(-4))  # should print error
