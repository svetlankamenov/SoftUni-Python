food_bought = int(input())
food_bought *= 1000

while True:
    food_eaten = input()
    if food_eaten == "Adopted" and food_bought >= 0:
        print(f"Food is enough! Leftovers: {abs(food_bought)} grams.")
        break
    elif food_eaten == "Adopted" and food_bought < 0:
        print(f"Food is not enough. You need {abs(food_bought)} grams more.")
        break

    food_eaten = int(food_eaten)
    food_bought -= food_eaten
