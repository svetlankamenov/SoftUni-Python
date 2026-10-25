is_even = True
count = int(input())

for _ in range(count):
    number = int(input())

    if number % 2 != 0:
        is_even = False

    if not is_even:
        print(f"{number} is odd!")
        break

if is_even:
    print("All numbers are even.")