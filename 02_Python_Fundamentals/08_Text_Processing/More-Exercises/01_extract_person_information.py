lines = []
n = int(input())


for i in range(n):
    lines.append(input())

for line in lines:
    start_i = line.find("@")
    end_i = line.find("|")
    name = line[start_i+1:end_i]

    start_i = line.find("#")
    end_i = line.find("*")
    age = line[start_i+1:end_i]

    print(f"{name} is {age} years old.")