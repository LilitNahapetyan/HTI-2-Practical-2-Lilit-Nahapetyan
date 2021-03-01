from datetime import datetime
import time

def warn_slow(func):
    def inner(*args, **kwargs):
        t1 = datetime.now()
        func(*args, **kwargs)
        t2 = datetime.now() - t1
        t = t2.total_seconds()
        if t < 2:
            return t
        else:
            x = f"Execution of {func.__name__} with arguments {args}, {kwargs} took more than 2 seconds"
            return x
    return inner

@warn_slow
def func_slow(x,y):
    time.sleep(3)

print(func_slow(1,2))

@warn_slow
def func_slow(x,y):
    time.sleep(1)

print(func_slow(1,2))
