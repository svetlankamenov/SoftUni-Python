def make_bold(function):
    def wrapper(*args, **kwargs):
        func_result = function(*args, **kwargs)
        return f"<b>{func_result}</b>"
    return wrapper


def make_italic(function):
    def wrapper(*args, **kwargs):
        func_result = function(*args, **kwargs)
        return f"<i>{func_result}</i>"
    return wrapper

def make_underline(function):
    def wrapper(*args, **kwargs):
        func_result = function(*args, **kwargs)
        return f"<u>{func_result}</u>"
    return wrapper


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))