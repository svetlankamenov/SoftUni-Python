#a + b + c = n
correct_solution = 0
n = int(input())

for a in range(0, n+1):
    for b in range(0, n+1):
        for c in range(0, n+1):
            if a + b + c == n:
                correct_solution += 1

print(correct_solution)