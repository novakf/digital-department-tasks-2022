import datetime

def time_decorator(func):
    def wrapper():
        before = datetime.datetime.now()
        res = func()
        print((datetime.datetime.now()-before).seconds)
        return res
    return wrapper