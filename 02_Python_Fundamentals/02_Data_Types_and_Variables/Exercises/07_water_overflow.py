poured_water = 0

n = int(input())

for _ in range(n):
    water_volume = int(input())

    if poured_water + water_volume > 255:
        print("Insufficient capacity!")
    else:
        poured_water += water_volume

print(poured_water)