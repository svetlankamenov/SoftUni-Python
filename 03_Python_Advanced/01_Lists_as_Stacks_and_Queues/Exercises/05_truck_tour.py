from collections import deque

tour_map = []

n = int(input())

for i in range(0, n):
    fuel, distance = map(int, input().split(" "))
    tour_map.append([i, fuel, distance])

tour_map = deque(tour_map)

start_station = 0
fuel_in_tank = 0

while len(tour_map) > 0:
    station = tour_map.popleft()
    i, fuel, distance = station
    fuel_in_tank += fuel

    if fuel_in_tank - distance < 0:
        fuel_in_tank = 0
        next_station = i + 1

        if next_station == n:
            start_station = 0
        else:
            start_station = next_station

        continue

    else:
        fuel_in_tank -= distance

print(start_station)