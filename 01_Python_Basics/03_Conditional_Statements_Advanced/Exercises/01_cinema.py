projection = input()
rows = int(input())
columns = int(input())
profit = 0.0

if projection.lower() == "premiere":
    profit = rows * columns * 12.00
    print(f"{profit:.2f} leva")

elif projection.lower() == "normal":
    profit = rows * columns * 7.50
    print(f"{profit:.2f} leva")

elif projection.lower() == "discount":
    profit = rows * columns * 5.00
    print(f"{profit:.2f} leva")