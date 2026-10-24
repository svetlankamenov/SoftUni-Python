first_player_eggs_count = int(input())
second_player_eggs_count = int(input())

while True:
    winner = input()

    if winner == "one":
        second_player_eggs_count -= 1
    elif winner == "two":
        first_player_eggs_count -= 1

    if first_player_eggs_count == 0:
        print(f"Player one is out of eggs. Player two has {second_player_eggs_count} eggs left.")
        break
    elif second_player_eggs_count == 0:
        print(f"Player two is out of eggs. Player one has {first_player_eggs_count} eggs left.")
        break

    if winner == "End":
        print(f"Player one has {first_player_eggs_count} eggs left.")
        print(f"Player two has {second_player_eggs_count} eggs left.")
        break