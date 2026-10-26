def separate_numbers(*args):
    p_sum = 0
    n_sum = 0

    for number in args:
        if number > 0:
            p_sum += number
        else:
            n_sum += number

    return p_sum, n_sum

numbers = list(map(int, input().split(" ")))

sum_of_positive_numbers, sum_of_negative_numbers = separate_numbers(*numbers)
print(sum_of_negative_numbers)
print(sum_of_positive_numbers)

if abs(sum_of_negative_numbers) > sum_of_positive_numbers:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")