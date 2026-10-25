def order_calculator(product: str, quantity: int):
    if product == "coffee":
        return quantity * 1.50
    elif product == "water":
        return quantity * 1.00
    elif product == "coke":
        return quantity * 1.40
    elif product == "snacks":
        return quantity * 2.00

product_input = input()
product_count = int(input())

print(f"{order_calculator(product_input, product_count):.2f}")