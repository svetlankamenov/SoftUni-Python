count = int(input())
min = 0
max = 0

for i in range(count):
    num = int(input())
    if i == 0:
        min = num
        max = num
        continue

    if num > max:
        max = num
    if num < min:
        min = num

print(f"Max number: {max}")
print(f"Min number: {min}")