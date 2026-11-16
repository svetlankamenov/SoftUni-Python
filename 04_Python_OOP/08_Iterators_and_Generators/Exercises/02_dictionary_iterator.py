class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = list(dictionary.items())
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current == len(self.dictionary):
            raise StopIteration
        return self.dictionary[self.current]

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)