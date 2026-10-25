best_snowball = 0
snowball_info = []
n = int(input())

for _ in range(n):
    snowball_weight = int(input())
    time = int(input())
    quality = int(input())

    snowball_value = (snowball_weight // time) ** quality
    if snowball_value > best_snowball:
        snowball_info.clear()
        best_snowball = snowball_value
        snowball_info.append(snowball_weight)
        snowball_info.append(time)
        snowball_info.append(quality)

print(f"{snowball_info[0]} : {snowball_info[1]} = {best_snowball} ({snowball_info[2]})")