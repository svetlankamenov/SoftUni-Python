sum_needed = int(input())
payment_counter = 0
payment_method = ""
income = 0
cash_payment = 0
card_payment = 0
cash_income = 0
card_income = 0

while True:
    payment_counter += 1
    if payment_counter % 2 != 0:
        payment_method = "cash"
    else:
        payment_method = "card"

    price = input()

    if not price == "End":
        price = int(price)

        if payment_method == "cash":
            if price <= 100:
                cash_income += price
                cash_payment += 1
                print("Product sold!")
            else:
                print("Error in transaction!")
                continue
        elif payment_method == "card":
            if price >= 10:
                card_income += price
                card_payment += 1
                print("Product sold!")
            else:
                print("Error in transaction!")
                continue

    else:
        print(f"Failed to collect required money for charity.")
        break

    income = cash_income + card_income
    if income >= sum_needed:
        print(f"Average CS: {(cash_income/cash_payment):.2f}")
        print(f"Average CC: {(card_income/card_payment):.2f}")
        break
