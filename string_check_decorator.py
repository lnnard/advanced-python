def string_check_decorator(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, str):
                print("Argument must be a string")
        return func(*args, **kwargs)
    return wrapper