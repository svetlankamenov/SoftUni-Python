budget_for_actors = float(input())
remuneration = 0.0

while True:
    actor_name = input()
    if actor_name == "ACTION":
        print(f"We are left with {budget_for_actors:.2f} leva.")
        break

    if len(actor_name) > 15:
        remuneration = budget_for_actors * 0.20
        budget_for_actors -= remuneration
    else:
        remuneration = float(input())
        budget_for_actors -= remuneration

    if budget_for_actors < 0:
        print(f"We need {abs(budget_for_actors):.2f} leva for our actors.")
        break