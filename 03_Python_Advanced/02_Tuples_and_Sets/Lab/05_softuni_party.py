guests = set()

n = int(input())

for _ in range(n):
    reservation_code = input()
    guests.add(reservation_code)

while True:
    reservation_code = input()

    if reservation_code == "END":
        break
    if reservation_code in guests:
        guests.remove(reservation_code)

sorted_guests = sorted(guests)

print(len(sorted_guests))

for guest in sorted_guests:
    print(guest)