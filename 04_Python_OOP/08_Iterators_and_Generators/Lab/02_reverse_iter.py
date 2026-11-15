class reverse_iter:
    def __init__(self, iter_input):
        self.iter_input = iter_input
        self.current = len(self.iter_input)

    def __iter__(self):
        return self

    def __next__(self):
        self.current -= 1
        if self.current < 0:
            raise StopIteration
        return self.iter_input[self.current]

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)