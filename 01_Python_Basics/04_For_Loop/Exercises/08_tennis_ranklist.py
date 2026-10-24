import math

tournament_count = int(input())
points = int(input())
points_won = 0
wins = 0

for _ in range(tournament_count):
    ending_position = input()

    if ending_position.lower() == "w":
        points += 2000
        wins += 1
        points_won += 2000
    elif ending_position.lower() == "f":
        points += 1200
        points_won += 1200
    elif ending_position.lower() == "sf":
        points += 720
        points_won += 720

print(f"Final points: {points}")
print(f"Average points: {math.floor(points_won/tournament_count)}")
print(f"{wins/tournament_count*100:.2f}%")