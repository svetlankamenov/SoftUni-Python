budged = float(input())
videocards = int(input())
cpus = int(input())
rams = int(input())

videocard_cost = 250 * videocards
cpu_cost = videocard_cost * cpus * 0.35
ram_cost = videocard_cost * rams * 0.10

total_cost = videocard_cost + cpu_cost + ram_cost

if videocards > cpus:
    total_cost *= 0.85

if budged >= total_cost:
    print(f"You have {budged-total_cost:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_cost-budged:.2f} leva more!")