from project.room import Room


class Hotel:
    def __init__(self, name:str):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([added_room.guests for added_room in self.rooms if added_room.is_taken])

    @classmethod
    def from_stars(cls, stars_count:int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room:Room):
        self.rooms.append(room)

    def take_room(self, room_number:int, people:int):
        for added_room in self.rooms:
            if added_room.number == room_number:
                added_room.take_room(people)

    def free_room(self, room_number:int):
        for added_room in self.rooms:
            if added_room.number == room_number:
                added_room.free_room()

    def status(self):
        free_rooms = [str(added_room.number) for added_room in self.rooms if not added_room.is_taken]
        taken_rooms = [str(added_room.number) for added_room in self.rooms if added_room.is_taken]

        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join(free_rooms)}\nTaken rooms: {', '.join(taken_rooms)}"
