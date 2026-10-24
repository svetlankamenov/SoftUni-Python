walking_minutes_per_day = int(input())
walking_counts = int(input())
cat_calories = int(input())

burned_calories = walking_counts * walking_minutes_per_day * 5
calories_target = cat_calories / 2

if burned_calories >= calories_target:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")