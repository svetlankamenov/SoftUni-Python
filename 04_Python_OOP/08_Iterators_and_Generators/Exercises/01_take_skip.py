class take_skip:
    def __init__(self, step:int, count:int):
        self.step = step
        self.count = count
        self.numbers_count = 0
        self.current_number = 0 - self.step

    def __iter__(self):
        return self

    def __next__(self):
        self.numbers_count += 1
        if self.numbers_count > self.count:
            raise StopIteration

        self.current_number += self.step
        return self.current_number

numbers = take_skip(10, 5)
for number in numbers:
    print(number)