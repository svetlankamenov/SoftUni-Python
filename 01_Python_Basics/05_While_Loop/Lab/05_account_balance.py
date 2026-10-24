balance = 0.0

while True:
    income = input()

    if income == "NoMoreMoney":
        print(f"Total: {balance:.2f}")
        break

    income = float(income)

    if income < 0:
        print("Invalid operation!")
        print(f"Total: {balance:.2f}")
        break

    balance += income
    print(f"Increase: {income:.2f}")