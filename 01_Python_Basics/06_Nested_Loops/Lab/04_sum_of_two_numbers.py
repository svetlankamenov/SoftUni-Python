#(a, b)
a = int(input())
b = int(input())
magic_number = int(input())
combination_number = 0
is_found = False

for i in range(a, b+1):
    for j in range(a, b+1):
        combination_number += 1
        if i + j == magic_number:
            print(f"Combination N:{combination_number} ({i} + {j} = {magic_number})")
            is_found = True
            break
    if is_found:
        break

if not is_found:
    print(f"{combination_number} combinations - neither equals {magic_number}")