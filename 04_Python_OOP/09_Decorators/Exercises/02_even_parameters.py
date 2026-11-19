def even_parameters(function):
    def wrapper(*args):
        for arg in args:
            try:
                if arg % 2 != 0:
                    return "Please use only even numbers!"
            except TypeError:
                return "Please use only even numbers!"
        result = function(*args)
        return result
    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))