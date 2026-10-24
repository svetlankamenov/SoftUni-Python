customer_bill = 0.0
customer_purchases_count = 0
total_income = 0.0

customers_count = int(input())

for _ in range(customers_count):

    while True:
        purchase = input()
        if purchase == "Finish":
            if customer_purchases_count % 2 == 0:
                customer_bill *= 0.80

            print(f"You purchased {customer_purchases_count} items for {customer_bill:.2f} leva." )
            total_income += customer_bill
            customer_bill = 0.0
            customer_purchases_count = 0
            break

        elif purchase == "basket":
            customer_bill += 1.50
            customer_purchases_count += 1

        elif purchase == "wreath":
            customer_bill += 3.80
            customer_purchases_count += 1

        elif purchase == "chocolate bunny":
            customer_bill += 7.00
            customer_purchases_count += 1

print(f"Average bill per client is: {total_income/customers_count:.2f} leva.")