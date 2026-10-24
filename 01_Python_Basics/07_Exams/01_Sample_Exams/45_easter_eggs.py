red_eggs_count = 0
orange_eggs_count = 0
blue_eggs_count = 0
green_eggs_count = 0
max_eggs = 0
max_eggs_colour = ""

eggs_count = int(input())

for _ in range(eggs_count):
    egg_colour = input()

    if egg_colour == "red":
        red_eggs_count += 1
    elif egg_colour == "orange":
        orange_eggs_count += 1
    elif egg_colour == "blue":
        blue_eggs_count += 1
    elif egg_colour == "green":
        green_eggs_count += 1

    if red_eggs_count > max_eggs:
        max_eggs = red_eggs_count
        max_eggs_colour = egg_colour
    elif orange_eggs_count > max_eggs:
        max_eggs = orange_eggs_count
        max_eggs_colour = egg_colour
    elif blue_eggs_count > max_eggs:
        max_eggs = blue_eggs_count
        max_eggs_colour = egg_colour
    elif green_eggs_count > max_eggs:
        max_eggs = green_eggs_count
        max_eggs_colour = egg_colour

print(f"Red eggs: {red_eggs_count}")
print(f"Orange eggs: {orange_eggs_count}")
print(f"Blue eggs: {blue_eggs_count}")
print(f"Green eggs: {green_eggs_count}")
print(f"Max eggs: {max_eggs} -> {max_eggs_colour}")