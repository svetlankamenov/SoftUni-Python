actor_name = input()
starting_points = float(input())
judge_count = int(input())

for _ in range(judge_count):
    judge_name = input()
    judge_points = float(input())

    gained_points = len(judge_name) * judge_points / 2
    starting_points += gained_points

    if starting_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {starting_points:.1f}!")
        break

if starting_points <= 1250.5:
    print(f"Sorry, {actor_name} you need {abs(starting_points-1250.5):.1f} more!")