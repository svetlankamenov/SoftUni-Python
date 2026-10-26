even_numbers = set()
odd_numbers = set()

n = int(input())

for i in range(1, n + 1):
    char_sum = 0
    name = input()

    for ch in name:
        char_sum += ord(ch)

    char_sum //= i

    if char_sum % 2 == 0:
        even_numbers.add(char_sum)
    else:
        odd_numbers.add(char_sum)

even_numbers_sum = sum(even_numbers)
odd_numbers_sum = sum(odd_numbers)

if even_numbers_sum == odd_numbers_sum:
    print(", ".join(map(str, odd_numbers.union(even_numbers))))
elif odd_numbers_sum > even_numbers_sum:
    print(", ".join(map(str, odd_numbers.difference(even_numbers))))
elif even_numbers_sum > odd_numbers_sum:
    print(", ".join(map(str, odd_numbers.symmetric_difference(even_numbers))))