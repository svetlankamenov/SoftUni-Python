def multiply(n):
    def decorator(function):
        def wrapper(*args, **kwargs):
            number = function(*args, **kwargs)
            return number*n
        return wrapper
    return decorator

@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))