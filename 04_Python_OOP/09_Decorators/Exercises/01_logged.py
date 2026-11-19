from functools import wraps


def logged(function):
    @wraps(function)
    def wrapper(*args):
        func_result = function(*args)
        result = f"you called {function.__name__}{args}\n"
        result += f"it returned {func_result}"
        return result
    return wrapper

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))