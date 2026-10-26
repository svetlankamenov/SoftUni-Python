def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key= lambda x: ((-len(x[1])), x[0]))

    result = ""

    for key, value in sorted_cheeses:
        value = sorted(value, reverse=True)
        result += key + "\n" + "\n".join(str(number) for number in value) + "\n"

    return result

print(sorting_cheeses(Parmesan=[102, 120, 135],Camembert=[100, 100, 105, 500, 430],Mozzarella=[50, 125]))