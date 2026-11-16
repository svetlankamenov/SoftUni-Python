class sequence_repeat:
    def __init__(self, sequence:str, number:int):
        self.sequence = sequence
        self.number = number
        self.current = -1
        self.new_sequence = sequence * (number // len(sequence) + 1)

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current == self.number:
            raise StopIteration
        return self.new_sequence[self.current]

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')