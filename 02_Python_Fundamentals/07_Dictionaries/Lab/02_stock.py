stock = {}
user_input = input().split(" ")
searched_products = input().split(" ")

for i in range(0, len(user_input), 2):
    key = user_input[i]
    value = user_input[i+1]
    stock[key] = int(value)

for product in searched_products:
    if product in stock.keys():
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")