trunk_capacity = float(input())
loaded_suitcases_count = 0
counter = 1

while True:
    suitcase_volume = input()
    if suitcase_volume == "End":
        print("Congratulations! All suitcases are loaded!")
        break

    suitcase_volume = float(suitcase_volume)

    if counter % 3 == 0:
        suitcase_volume *= 1.10

    if trunk_capacity - suitcase_volume >= 0:
        loaded_suitcases_count += 1
        trunk_capacity -= suitcase_volume
    else:
        print("No more space!")
        break

    counter += 1

print(f"Statistic: {loaded_suitcases_count} suitcases loaded.")