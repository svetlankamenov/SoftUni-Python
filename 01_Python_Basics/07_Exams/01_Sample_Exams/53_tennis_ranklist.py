import math

tournament = int(input())
start_up_points = int(input())
earned_points = 0
wins = 0

for _ in range(tournament):
    stage = input()

    if stage == "W":
        earned_points += 2000
        wins += 1

    elif stage == "F":
        earned_points += 1200

    elif stage == "SF":
        earned_points += 720

print(f"Final points: {start_up_points + earned_points}")
print(f"Average points: {math.floor(earned_points / tournament)}")
print(f"{(wins / tournament * 100):.2f}%")
