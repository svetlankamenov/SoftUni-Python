first_player = input()
second_player = input()
first_player_score = 0
second_player_score = 0

while True:
    first_card = input()
    if first_card == "End of game":
        print(f"{first_player} has {first_player_score} points")
        print(f"{second_player} has {second_player_score} points")
        break

    second_card = input()

    if int(first_card) > int(second_card):
        first_player_score += int(first_card) - int(second_card)
    elif int(first_card) < int(second_card):
        second_player_score += int(second_card) - int(first_card)
    elif int(first_card) == int(second_card):
        print("Number wars!")
        first_card = input()
        second_card = input()
        if int(first_card) > int(second_card):
            print(f"{first_player} is winner with {first_player_score} points")
        else:
            print(f"{second_player} is winner with {second_player_score} points")
        break