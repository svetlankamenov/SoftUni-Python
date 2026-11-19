def number_increment(lst:list):
    def increase():
        increased_lst = [num + 1 for num in lst]
        return increased_lst

    return increase()

print(number_increment([1, 2, 3]))