best_player_name = ""
best_player_score = 0

while True:
    player_name = input()
    if player_name == "END":
        print(f"{best_player_name} is the best player!")

        if best_player_score >= 3:
            print(f"He has scored {best_player_score} goals and made a hat-trick !!!")
        else:
            print(f"He has scored {best_player_score} goals.")
        break

    player_score = int(input())

    if player_score > best_player_score:
        best_player_name = player_name
        best_player_score = player_score

    if player_score >= 10:
        print(f"{best_player_name} is the best player!")
        print(f"He has scored {best_player_score} goals and made a hat-trick !!!")
        break