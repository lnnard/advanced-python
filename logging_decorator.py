def logging_decorator(function):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        if args:
            print(f"Function {function.__name__} was called with arguments: {args}")
        elif kwargs:
            print(f"Function {function.__name__} was called with keyword arguments: {kwargs}")
        else:
            print(f"Function {function.__name__} was called without arguments")
    return wrapper