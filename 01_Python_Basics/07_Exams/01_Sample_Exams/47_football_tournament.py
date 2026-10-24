wins_count = 0
draws_count = 0
losses_count = 0
team_points = 0

team_name = input()
played_games = int(input())

for _ in range(played_games):
    result = input()

    if result == 'W':
        wins_count += 1
        team_points += 3
    elif result == 'D':
        draws_count += 1
        team_points += 1
    elif result == 'L':
        losses_count += 1

if played_games == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    print(f"{team_name} has won {team_points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins_count}")
    print(f"## D: {draws_count}")
    print(f"## L: {losses_count}")
    print(f"Win rate: {wins_count / played_games * 100:.2f}%")