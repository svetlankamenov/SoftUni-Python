orders = {}

while True:
    product = input()
    if product == "buy":
        for product in orders.keys():
            print(f"{product} -> {orders[product]['price']*orders[product]['quantity']:.2f}")
        break

    product_name, price, quantity = product.split(" ")

    if product_name not in orders:
        orders[product_name] = {"price": float(price), "quantity": int(quantity)}
    else:
        orders[product_name]["price"] = float(price)
        orders[product_name]["quantity"] += int(quantity)