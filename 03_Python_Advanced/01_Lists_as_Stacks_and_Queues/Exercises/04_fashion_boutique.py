racks_count = 1

clothes = list(map(int, input().split(" ")))
capacity_of_rack = int(input())

current_clothes_in_rack = 0

while len(clothes) != 0:
    clothes_count = clothes.pop()
    if (current_clothes_in_rack + clothes_count) > capacity_of_rack:
        racks_count += 1
        current_clothes_in_rack = clothes_count
    elif (current_clothes_in_rack + clothes_count) == capacity_of_rack and len(clothes) != 0:
        racks_count += 1
        current_clothes_in_rack = 0
    else:
        current_clothes_in_rack += clothes_count

print(racks_count)