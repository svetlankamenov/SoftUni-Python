voucher = int(input())
cost = 0
ticket_counter = 0
other_purchases = 0

while True:
    purchase = input()

    if not purchase == "End":
        #Ако е филм
        if len(purchase) >  8:
            cost = ord(purchase[0]) + ord(purchase[1])
            if cost <= voucher:
                ticket_counter += 1
                voucher -= cost
            else:
                print(ticket_counter)
                print(other_purchases)
                break
        #Ако е друга покупка
        else:
            cost = ord(purchase[0])
            if cost <= voucher:
                other_purchases += 1
                voucher -= cost
            else:
                print(ticket_counter)
                print(other_purchases)
                break
    else:
        print(ticket_counter)
        print(other_purchases)
        break