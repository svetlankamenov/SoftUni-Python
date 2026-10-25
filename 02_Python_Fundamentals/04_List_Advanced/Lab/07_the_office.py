happiness_input = input().split(" ")
improvement_factor = int(input())

happiness_input = list(map(int, happiness_input))
employees_happiness = list(map(lambda x: x * improvement_factor, happiness_input))
happiness_above_average = list(filter(lambda x: x >= (sum(employees_happiness)/len(employees_happiness)), employees_happiness))

if len(happiness_above_average) >= len(employees_happiness) / 2:
    print(f"Score: {len(happiness_above_average)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happiness_above_average)}/{len(employees_happiness)}. Employees are not happy!")