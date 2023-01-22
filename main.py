import time


def measure_time(func):
    def inner():
        start = time.time()
        result = func()
        print(time.time() - start)
        return result
    return inner


def deprecated(message1):
    def decorator(fun):
        print(message1)
        def wrapper(*args, **kwargs):
            return fun(*args, **kwargs)
        return wrapper
    return decorator


def min_value(value):
    def decorator(fun):
        def wrapper(param1):
            if param1 < value:
                raise AttributeError()
            return fun(param1)
        return wrapper
    return decorator


@deprecated("Function is Deprecated")
@min_value(10)
def mult_by_4(x):
    for i in range(1, 100):
        x += i
    return x


class Builder:
    def __init__(self, cls):
        def get_builder():
            return "Builder"
        self.builder = get_builder


@Builder
class Car:
    def __int__(self, ps, name):
        self.ps = ps
        self.name = name



if __name__ == '__main__':
    print(Car.builder())
