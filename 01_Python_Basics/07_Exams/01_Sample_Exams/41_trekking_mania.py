musala_group = 0
mont_blanc_group = 0
kilimanjaro_group = 0
k2_group = 0
everest_group = 0
total_people = 0

groups_count = int(input())

for _ in range(groups_count):
    people_count = int(input())
    total_people += people_count

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

print(f"{musala_group/total_people*100:.2f}%")
print(f"{mont_blanc_group/total_people*100:.2f}%")
print(f"{kilimanjaro_group/total_people*100:.2f}%")
print(f"{k2_group/total_people*100:.2f}%")
print(f"{everest_group/total_people*100:.2f}%")
