def squares(end:int):
    n = 1
    while n <= end:
        yield n ** 2
        n += 1

print(list(squares(5)))