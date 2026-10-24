back_trainers = 0
chest_trainers = 0
leg_trainers = 0
abs_trainers = 0
protein_shake = 0
protein_bar = 0

visitors = int(input())

for _ in range(visitors):
    action = input()

    if action == "Back":
        back_trainers += 1
    elif action == "Chest":
        chest_trainers += 1
    elif action == "Legs":
        leg_trainers += 1
    elif action == "Abs":
        abs_trainers += 1
    elif action == "Protein shake":
        protein_shake += 1
    elif action == "Protein bar":
        protein_bar += 1

eaters = protein_bar + protein_shake
trainers = visitors - eaters

print(f"{back_trainers} - back")
print(f"{chest_trainers} - chest")
print(f"{leg_trainers} - legs")
print(f"{abs_trainers} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{(trainers/visitors*100):.2f}% - work out")
print(f"{(eaters/visitors*100):.2f}% - protein")