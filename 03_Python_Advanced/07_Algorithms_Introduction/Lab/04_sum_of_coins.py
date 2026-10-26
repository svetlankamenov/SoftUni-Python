def choose_coins(coins:list, target_sum:int):
    coins.sort(reverse=True)
    i = 0
    used_coins = {}

    while target_sum != 0 and i < len(coins):
        count_coins = target_sum // coins[i]
        target_sum %= coins[i]

        if count_coins > 0:
            used_coins[coins[i]] = count_coins

        i += 1

    if target_sum == 0:
        result = f"Number of coins to take: {sum(used_coins.values())}\n"

        for value, count in used_coins.items():
            result += f"{count} coin(s) with value {value}\n"
        result = result.strip()

        return result

    else:
        return "Error"

possible_coins = list(map(int, input().split(", ")))
t_sum = int(input())

print(choose_coins(possible_coins, t_sum))