string = input()
new_string = ""

for i in range(len(string)):
    if i == 0:
        new_string += string[i]
    else:
        if string[i] != new_string[len(new_string) - 1]:
            new_string += string[i]

print(new_string)