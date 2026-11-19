def cache(function):
    log = {}
    def wrapper(*args):
        n = args[0]
        if n not in log:
            log[n] = function(n)
        return log[n]

    wrapper.log = log
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(3)
print(fibonacci.log)