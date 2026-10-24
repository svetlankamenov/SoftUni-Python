x = float(input())
y = float(input())
h = float(input())

walls = (2 * x * x) + (2 * x * y) - (1.2 * 2) - (2 * 1.5 * 1.5)
roof = (2 * x * y) + (x * h)

green_dye = walls / 3.4
red_dye = roof / 4.3

print(f"{green_dye:.2f}")
print(f"{red_dye:.2f}")


