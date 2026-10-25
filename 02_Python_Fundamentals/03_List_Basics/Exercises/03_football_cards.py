team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
terminate = False

game_result = input()
game_cards = game_result.split(" ")

for card in game_cards:
    if "A" in card:
        if int(card[2:]) in team_a:
            team_a.remove(int(card[2:]))
    elif "B" in card:
        if int(card[2:]) in team_b:
            team_b.remove(int(card[2:]))

    if len(team_a) < 7 or len(team_b) < 7:
        terminate = True
        break

if terminate:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
    print("Game was terminated")
else:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
