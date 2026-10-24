import math

painted_area = 0
wall_height = int(input())
wall_width = int(input())
area_not_for_painting = int(input())


area_for_painting = wall_height * wall_width * 4
area_for_painting -= area_for_painting * area_not_for_painting / 100
area_for_painting = math.ceil(area_for_painting)

while True:
    dye_liters = input()
    if dye_liters == "Tired!":
        print(f"{abs(painted_area-area_for_painting)} quadratic m left.")
        break

    dye_liters = int(dye_liters)
    painted_area += dye_liters

    if painted_area > area_for_painting:
        print(f"All walls are painted and you have {abs(painted_area-area_for_painting)} l paint left!")
        break
    elif painted_area - area_for_painting == 0:
        print("All walls are painted! Great job, Pesho!")
        break