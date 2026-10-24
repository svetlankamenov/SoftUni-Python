floors_count = int(input())
rooms_count = int(input())
room_type = "L"

for floor in range(floors_count, 0, -1):
    if not floor == floors_count:
        if floor % 2 == 0:
            room_type = "O"
        else:
            room_type = "A"

    for room in range(0, rooms_count):
        print(f"{room_type}{floor}{room}", end=" ")
    print()