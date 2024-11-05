
def devide(func):
    def wrapper(a,b):
        res = func(a,b) / 2
        return res
    return wrapper

@devide
def add_num(a,b):
    return a + b


print(add_num(5,5))