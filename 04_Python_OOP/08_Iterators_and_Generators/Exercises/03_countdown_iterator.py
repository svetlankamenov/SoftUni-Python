class countdown_iterator:
    def __init__(self, count:int):
        self.count = count
        self.number = self.count + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number -= 1
        if self.number < 0:
            raise StopIteration
        return self.number

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")