from math import pi

figure = input()
area = 0.0

if figure.lower() == "square":
    a = float(input())
    area = a * a
    print(f"{area:.3f}")
elif figure.lower() == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    print(f"{area:.3f}")
elif figure.lower() == "circle":
    r = float(input())
    area = pi * r * r
    print(f"{area:.3f}")
elif figure.lower() == "triangle":
    a = float(input())
    h = float(input())
    area = a * h / 2
    print(f"{area:.3f}")