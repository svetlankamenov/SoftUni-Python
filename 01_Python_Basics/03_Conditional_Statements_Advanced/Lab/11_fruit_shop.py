fruit = input()
day = input()
quantity = float(input())
price = 0.0

if (day.lower() == "monday" or day.lower() == "tuesday"
        or day.lower() == "wednesday" or day.lower() == "thursday"
        or day.lower() == "friday"):

    if fruit.lower() == "banana":
        price = quantity * 2.50
        print(f"{price:.2f}")
    elif fruit.lower() == "apple":
        price = quantity * 1.20
        print(f"{price:.2f}")
    elif fruit.lower() == "orange":
        price = quantity * 0.85
        print(f"{price:.2f}")
    elif fruit.lower() == "grapefruit":
        price = quantity * 1.45
        print(f"{price:.2f}")
    elif fruit.lower() == "kiwi":
        price = quantity * 2.70
        print(f"{price:.2f}")
    elif fruit.lower() == "pineapple":
        price = quantity * 5.50
        print(f"{price:.2f}")
    elif fruit.lower() == "grapes":
        price = quantity * 3.85
        print(f"{price:.2f}")
    else:
        print("error")

elif (day.lower() == "saturday" or day.lower() == "sunday"):

    if fruit.lower() == "banana":
        price = quantity * 2.70
        print(f"{price:.2f}")
    elif fruit.lower() == "apple":
        price = quantity * 1.25
        print(f"{price:.2f}")
    elif fruit.lower() == "orange":
        price = quantity * 0.90
        print(f"{price:.2f}")
    elif fruit.lower() == "grapefruit":
        price = quantity * 1.60
        print(f"{price:.2f}")
    elif fruit.lower() == "kiwi":
        price = quantity * 3.00
        print(f"{price:.2f}")
    elif fruit.lower() == "pineapple":
        price = quantity * 5.60
        print(f"{price:.2f}")
    elif fruit.lower() == "grapes":
        price = quantity * 4.20
        print(f"{price:.2f}")
    else:
        print("error")

else:
    print("error")