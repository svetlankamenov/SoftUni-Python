bakery = {}
user_input = input().split(" ")

for i in range(0, len(user_input), 2):
    key = user_input[i]
    value = user_input[i+1]
    bakery[key] = int(value)

print(bakery)