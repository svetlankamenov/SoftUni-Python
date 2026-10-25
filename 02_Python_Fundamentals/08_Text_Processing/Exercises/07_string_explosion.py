i = 0
strength = 0

string = list(input())

while i < len(string):
    if string[i] == ">":
        strength += int(string[i+1])
        i += 1
    elif strength > 0:
        strength -= 1
        string.pop(i)
    else:
        i += 1

print("".join(string))