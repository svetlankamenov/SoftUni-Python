city = input()
profit = float(input())
commission = 0.0

if city.lower() == "sofia":

    if profit >= 0 and profit <= 500:
        commission = profit * 0.05
        print(f"{commission:.2f}")
    elif profit > 500 and profit <= 1000:
        commission = profit * 0.07
        print(f"{commission:.2f}")
    elif profit > 1000 and profit <= 10000:
        commission = profit * 0.08
        print(f"{commission:.2f}")
    elif profit > 10000:
        commission = profit * 0.12
        print(f"{commission:.2f}")
    else:
        print("error")

elif city.lower() == "varna":

    if profit >= 0 and profit <= 500:
        commission = profit * 0.045
        print(f"{commission:.2f}")
    elif profit > 500 and profit <= 1000:
        commission = profit * 0.075
        print(f"{commission:.2f}")
    elif profit > 1000 and profit <= 10000:
        commission = profit * 0.10
        print(f"{commission:.2f}")
    elif profit > 10000:
        commission = profit * 0.13
        print(f"{commission:.2f}")
    else:
        print("error")

elif city.lower() == "plovdiv":

    if profit >= 0 and profit <= 500:
        commission = profit * 0.055
        print(f"{commission:.2f}")
    elif profit > 500 and profit <= 1000:
        commission = profit * 0.08
        print(f"{commission:.2f}")
    elif profit > 1000 and profit <= 10000:
        commission = profit * 0.12
        print(f"{commission:.2f}")
    elif profit > 10000:
        commission = profit * 0.145
        print(f"{commission:.2f}")
    else:
        print("error")

else:
    print("error")