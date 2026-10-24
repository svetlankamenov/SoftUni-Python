trip_cost = float(input())
balance = float(input())
past_days = 0
stop_threshold = 0

while True:
    action = input()
    money = float(input())

    if action == "spend":
        stop_threshold += 1
        if balance - money < 0:
            balance = 0
        else:
            balance -= money
    elif action == "save":
        balance += money
        stop_threshold = 0

    past_days += 1

    if stop_threshold == 5:
        print("You can't save the money.")
        print(past_days)
        break

    if balance >= trip_cost:
        print(f"You saved the money for {past_days} days.")
        break