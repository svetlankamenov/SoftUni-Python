class vowels:
    VOWELS = ("a", "e", "i", "o", "u", "y")

    def __init__(self, string:str):
        self.string = string
        self.current = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current >= len(self.string):
            raise StopIteration
        if self.string[self.current].lower() in self.VOWELS:
            return self.string[self.current]
        else:
            return self.__next__()

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)