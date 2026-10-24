saved_money = 0.0

while True:
    destination = input()
    if destination == "End":
        break

    budget = float(input())

    while True:
        income = float(input())
        saved_money += income
        if saved_money >= budget:
            print(f"Going to {destination}!")
            saved_money = 0.0
            break