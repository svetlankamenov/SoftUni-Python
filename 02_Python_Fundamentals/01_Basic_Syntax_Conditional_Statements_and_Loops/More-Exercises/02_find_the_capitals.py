list = []

string = input()

for i in range(len(string)):
    if "A" <= string[i] <= "Z":
        list.append(i)

print(list)