def double_decorator(funtion):
    def wrapper():
        funtion()
        funtion()
    return wrapper