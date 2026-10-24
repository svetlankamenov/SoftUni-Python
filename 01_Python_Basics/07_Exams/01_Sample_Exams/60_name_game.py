winner = ""
best_score = 0
current_score = 0

while True:
    player_name = input()
    if player_name == "Stop":
        break

    for i in player_name:
        number = int(input())
        if number == ord(i):
            current_score += 10
        else:
            current_score += 2

    if current_score >= best_score:
        best_score = current_score
        winner = player_name

    current_score = 0
print(f"The winner is {winner} with {best_score} points!")