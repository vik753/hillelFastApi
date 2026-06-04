```py
import math


def myltiplay_with_exceptions(fn):
    def wrapper(*args, **kwargs):
        try:
            correct_args = tuple(map(float, args))
            correct_kwargs = {key: float(val) for key, val in kwargs.items()}
            return fn(*correct_args, **correct_kwargs)
        except Exception as err:
            print(f"Incorrect function arguments: {err}")

    return wrapper


@myltiplay_with_exceptions
def multiply(*args, **kwargs):
    return math.prod(args + tuple(kwargs.values()))


print(multiply(2, 3, 2))
print(multiply("2", "3", "2"))
print(multiply(a=2, b=3))
print(multiply(2))
print(multiply("s", "d"))
```