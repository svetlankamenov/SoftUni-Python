def even_odd_filter(**kwargs):
    if "odd" in kwargs:
        odd_numbers = [num for num in kwargs["odd"] if num % 2 != 0]
        kwargs["odd"] = odd_numbers

    if "even" in kwargs:
        even_numbers = [num for num in kwargs["even"] if num % 2 == 0]
        kwargs["even"] = even_numbers

    dictionary = dict(sorted(kwargs.items(), key=lambda x: x[1], reverse=True))
    return dictionary

print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5],even=[3, 4, 5, 7, 10, 2, 5, 5, 2]))
print(even_odd_filter(odd=[2, 2, 30, 44, 10, 5]))