integers = input().split(" ")
reversed_integers = []

for _ in range(len(integers)):
    reversed_integers.append(integers.pop())

print(" ".join(reversed_integers))