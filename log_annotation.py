from stack import Stack
from functools import wraps


def log(stack=Stack()):
    def log_decorator(func):
        @wraps(func)
        def logging(*args, **kwargs):
            log_entry = """calling function: {0}
description: {1}
params: {2}""".format(func.__name__, func.__doc__, *args)
            stack.push(log_entry)
            return func(*args, **kwargs)
        return logging
    return log_decorator
