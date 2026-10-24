width = int(input())
length = int(input())
height = int(input())

apartment_space = width * length * height

while apartment_space > 0:
    boxes = input()

    if boxes == "Done":
        print(f"{apartment_space} Cubic meters left.")
        break

    boxes = int(boxes)
    apartment_space -= boxes

    if apartment_space <= 0:
        print(f"No more free space! You need {abs(apartment_space)} Cubic meters more.")
        break