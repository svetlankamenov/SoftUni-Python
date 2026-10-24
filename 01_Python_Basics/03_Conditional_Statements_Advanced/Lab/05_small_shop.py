product = input()
city = input()
quantity = float(input())
price = 0.0

if city.lower() == "sofia":
    if product.lower() == "coffee":
        price = quantity * 0.50
    elif product.lower() == "water":
        price = quantity * 0.80
    elif product.lower() == "beer":
        price = quantity * 1.20
    elif product.lower() == "sweets":
        price = quantity * 1.45
    elif product.lower() == "peanuts":
        price = quantity * 1.60

elif city.lower() == "plovdiv":
    if product.lower() == "coffee":
        price = quantity * 0.40
    elif product.lower() == "water":
        price = quantity * 0.70
    elif product.lower() == "beer":
        price = quantity * 1.15
    elif product.lower() == "sweets":
        price = quantity * 1.30
    elif product.lower() == "peanuts":
        price = quantity * 1.50

elif city.lower() == "varna":
    if product.lower() == "coffee":
        price = quantity * 0.45
    elif product.lower() == "water":
        price = quantity * 0.70
    elif product.lower() == "beer":
        price = quantity * 1.10
    elif product.lower() == "sweets":
        price = quantity * 1.35
    elif product.lower() == "peanuts":
        price = quantity * 1.55

print(price)