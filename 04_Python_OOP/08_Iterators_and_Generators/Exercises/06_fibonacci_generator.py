def fibonacci():
    i = 1
    numbers_collection = [0, 1]
    while True:
        numbers_collection.append(numbers_collection[i] + numbers_collection[i-1])
        yield numbers_collection[i-1]
        i += 1

generator = fibonacci()
for i in range(1):
    print(next(generator))