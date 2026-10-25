purchases_cost = 0

budget = int(input())

while True:
    price = input()
    if price == "End":
        print("You bought everything needed.")
        break

    price = int(price)
    purchases_cost += price

    if budget - purchases_cost < 0:
        print("You went in overdraft!")
        break