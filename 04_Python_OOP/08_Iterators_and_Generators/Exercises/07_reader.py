def read_next(*args):
    for iterable_object in args:
        for ch in iterable_object:
            yield ch

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)