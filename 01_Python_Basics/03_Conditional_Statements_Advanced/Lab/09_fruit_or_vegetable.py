product = input()

if (product.lower() == "banana" or product.lower() == "apple"
        or product.lower() == "kiwi" or product.lower() == "cherry"
        or product.lower() == "lemon" or product.lower() == "grapes"):
    print("fruit")

elif (product.lower() == "tomato" or product.lower() == "cucumber"
      or product.lower() == "pepper" or product.lower() == "carrot"):
    print("vegetable")

else:
    print("unknown")