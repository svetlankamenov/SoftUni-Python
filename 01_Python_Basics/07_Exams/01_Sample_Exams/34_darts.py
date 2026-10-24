score = 0
successful_shot = 0
unsuccessful_shot = 0

player_name = input()

while True:
    area = input()
    if area == "Retire":
        print(f"{player_name} retired after {unsuccessful_shot} unsuccessful shots.")
        break

    points = int(input())

    if area == "Single":
        score += points
        if 301 - score < 0:
            score -= points
            unsuccessful_shot += 1
            continue
        else:
            successful_shot += 1

    elif area == "Double":
        score += points * 2
        if 301 - score < 0:
            score -= points * 2
            unsuccessful_shot += 1
            continue
        else:
            successful_shot += 1

    elif area == "Triple":
        score += points * 3
        if 301 - score < 0:
            score -= points * 3
            unsuccessful_shot += 1
            continue
        else:
            successful_shot += 1

    if score - 301 == 0:
        print(f"{player_name} won the leg with {successful_shot} shots.")
        break