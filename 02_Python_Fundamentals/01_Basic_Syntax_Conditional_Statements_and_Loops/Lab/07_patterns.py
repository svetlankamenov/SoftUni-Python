num = int(input())

for i in range(1, 2*num):
    if i <= num:
        for j in range(0, i):
            print("*", end="")
        print()
    else:
        for j in range(0, 2*num-i):
            print("*", end="")
        print()