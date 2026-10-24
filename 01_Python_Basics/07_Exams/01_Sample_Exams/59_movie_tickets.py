a1 = int(input())
a2 = int(input())
n = int(input())
first_symbol = ""
second_symbol = 0
third_symbol = 0
fourth_symbol = 0

for i in range(a1, a2):
    if not i % 2 == 0:
        first_symbol = chr(i)

        for j in range(1, n):
            for k in range(1, (n//2 - 1) + 1):
                if not (j + k + i) % 2 == 0:
                    second_symbol = j
                    third_symbol = k
                    fourth_symbol = i

                    print(f"{first_symbol}-{second_symbol}{third_symbol}{fourth_symbol}" )
                else:
                    continue
    else:
        continue