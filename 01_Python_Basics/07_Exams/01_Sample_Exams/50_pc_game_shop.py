hearthstone_sales = 0
fornite_sales = 0
overwatch_sales = 0
others_sales = 0

sold_games = int(input())

for _ in range(sold_games):
    game_name = input()

    if game_name == "Hearthstone":
        hearthstone_sales += 1
    elif game_name == "Fornite":
        fornite_sales += 1
    elif game_name == "Overwatch":
        overwatch_sales += 1
    else:
        others_sales += 1

print(f"Hearthstone - {hearthstone_sales/sold_games*100:.2f}%")
print(f"Fornite - {fornite_sales/sold_games*100:.2f}%")
print(f"Overwatch - {overwatch_sales/sold_games*100:.2f}%")
print(f"Others - {others_sales/sold_games*100:.2f}%")