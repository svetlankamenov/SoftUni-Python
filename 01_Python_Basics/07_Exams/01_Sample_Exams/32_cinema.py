hall_seats_count = int(input())
people_count = 0
cinema_profit = 0

while True:
    people_in = input()
    if people_in == "Movie time!":
        print(f"There are {hall_seats_count-people_count} seats left in the cinema.")
        break

    people_in = int(people_in)

    if people_in + people_count > hall_seats_count:
        print("The cinema is full.")
        break

    people_count += people_in

    if people_in % 3 == 0:
        cinema_profit += (people_in * 5) - 5
    else:
        cinema_profit += people_in * 5

print(f"Cinema income - {cinema_profit} lv.")