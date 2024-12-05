def logging_decorator(function):
    def wrapper():
        function()
        print(f"Function {function.__name__} was called")
    return wrapper