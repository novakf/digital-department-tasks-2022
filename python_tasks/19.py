import datetime
from inspect import getcallargs

def logging_decorator(logger):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time = datetime.datetime.now()
            res = func(*args, **kwargs)
            logger.append({
                "name": func.__name__,
                "arguments": getcallargs(func, *args, **kwargs),
                "call_time": time,
                "result": res
            })
            return res
        return wrapper
    return decorator