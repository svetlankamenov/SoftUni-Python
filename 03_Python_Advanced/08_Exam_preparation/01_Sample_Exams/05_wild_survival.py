from collections import deque

bee_groups = deque(int(x) for x in input().split())
bee_eaters_group = [int(x) for x in input().split()]

while bee_groups and bee_eaters_group:
    bees = bee_groups.popleft()
    eaters = bee_eaters_group.pop()

    while bees >= 7 and eaters > 0:
        bees -= 7
        eaters -= 1

    if bees > 0 and eaters == 0:
        bee_groups.append(bees)
    elif eaters > 0 and bees < 7:
        bee_eaters_group.append(eaters)

print("The final battle is over!")
if not bee_groups and not bee_eaters_group:
    print("But no one made it out alive!")
else:
    if bee_groups:
        print("Bee groups left: ", end="")
        print(", ".join(map(str, bee_groups)))
    if bee_eaters_group:
        print("Bee-eater groups left: ", end="")
        print(", ".join(map(str, bee_eaters_group)))