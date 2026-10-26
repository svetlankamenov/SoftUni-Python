def accommodate(*args, **kwargs):
    output = ""
    unsuccessful_accommodations = 0
    checked_in_guests = []
    available_rooms = sorted(kwargs.items(), key=lambda x: (x[1], x[0]))

    for group in args:
        for room in available_rooms:
            if room[1] >= group:
                checked_in_guests.append((room[0], group))
                available_rooms.remove(room)
                break
        else:
            unsuccessful_accommodations += group

    checked_in_guests = sorted(checked_in_guests, key=lambda x: x[0])

    if checked_in_guests:
        output += f"A total of {len(checked_in_guests)} accommodations were completed!\n"
        for room, count in checked_in_guests:
            room_number = room.split("_")[1]
            output += f"<Room {room_number} accommodates {count} guests>\n"
    else:
        output += "No accommodations were completed!\n"

    if unsuccessful_accommodations != 0:
        output += f"Guests with no accommodation: {unsuccessful_accommodations}\n"
    if len(available_rooms) != 0:
        output += f"Empty rooms: {len(available_rooms)}"

    output = output.rstrip()

    return output