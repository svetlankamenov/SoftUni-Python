products = {}
count_of_all_products = 0
quantity_of_all_products = 0

while True:
    new_product = input()
    if new_product == "statistics":

        print("Products in stock:")

        for product, quantity in products.items():
            print(f"- {product}: {quantity}")
            count_of_all_products += 1
            quantity_of_all_products += quantity

        print(f"Total Products: {count_of_all_products}")
        print(f"Total Quantity: {quantity_of_all_products}")

        break

    new_product = new_product.split(": ")
    key = new_product[0]
    value = int(new_product[1])

    if key not in products:
        products[key] = value
    else:
        products[key] += value
