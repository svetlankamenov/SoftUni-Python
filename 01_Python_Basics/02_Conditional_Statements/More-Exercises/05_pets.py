import math

trip_days = int(input())
pet_food = int(input())
dog_eating = float(input())
cat_eating = float(input())
turtle_eating = float(input())

food_consumption = trip_days * (dog_eating + cat_eating + (turtle_eating/1000))
difference = abs(food_consumption - pet_food)

if food_consumption < pet_food:
    print(f"{math.floor(difference)} kilos of food left.")
else:
    print(f"{math.ceil(difference)} more kilos of food are needed.")