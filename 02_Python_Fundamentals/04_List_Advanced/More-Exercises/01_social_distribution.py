difference = 0

population = input().split(", ")
population = list(map(int, population))

minimum_wealth = int(input())

if (sum(population) / len(population)) >= minimum_wealth:
    for i in range(len(population)):
        the_wealthiest = max(population)
        index_the_wealthiest = population.index(the_wealthiest)

        if population[i] < minimum_wealth:
            difference = minimum_wealth - population[i]
            the_wealthiest = the_wealthiest - difference
            population[i] += difference
            population[index_the_wealthiest] = the_wealthiest

    print(population)
else:
    print("No equal distribution possible")