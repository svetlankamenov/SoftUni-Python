days_count = int(input())
food_quantity = float(input())
food_eaten_by_dog = 0
food_eaten_by_cat = 0
total_eaten_food = 0
cookies_quantity = 0

for i in range(1, days_count+1):
    dog_food = int(input())
    cat_food = int(input())

    food_eaten_by_dog += dog_food
    food_eaten_by_cat += cat_food

    if i % 3 == 0:
        cookies_quantity += (dog_food + cat_food) * 0.10

    total_eaten_food += dog_food + cat_food

print(f"Total eaten biscuits: {round(cookies_quantity)}gr.")
print(f"{total_eaten_food/food_quantity*100:.2f}% of the food has been eaten.")
print(f"{food_eaten_by_dog/total_eaten_food*100:.2f}% eaten from the dog.")
print(f"{food_eaten_by_cat/total_eaten_food*100:.2f}% eaten from the cat.")
