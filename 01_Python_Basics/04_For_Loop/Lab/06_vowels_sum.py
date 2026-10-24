text = input()
sum = 0

for char in text:
    if char.lower() == "a":
        sum += 1
    elif char.lower() == "e":
        sum += 2
    elif char.lower() == "i":
        sum += 3
    elif char.lower() == "o":
        sum += 4
    elif char.lower() == "u":
        sum += 5

print(sum)