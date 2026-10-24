group_count = int(input())
total_people_count = 0
musala_group = 0
mont_blanc_group = 0
kilimanjaro_group = 0
k2_group = 0
everest_group = 0

for _ in range(group_count):
    people_count = int(input())

    if people_count <= 5:
        musala_group += people_count
    elif 6 <= people_count <= 12:
        mont_blanc_group += people_count
    elif 13 <= people_count <= 25:
        kilimanjaro_group += people_count
    elif 26 <= people_count <= 40:
        k2_group += people_count
    elif people_count >= 41:
        everest_group += people_count

    total_people_count += people_count

print(f"{musala_group/total_people_count*100:.2f}%")
print(f"{mont_blanc_group/total_people_count*100:.2f}%")
print(f"{kilimanjaro_group/total_people_count*100:.2f}%")
print(f"{k2_group/total_people_count*100:.2f}%")
print(f"{everest_group/total_people_count*100:.2f}%")