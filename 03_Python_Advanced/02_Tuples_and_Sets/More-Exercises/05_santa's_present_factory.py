from collections import deque

presents_info = {
    "Doll" : 150,
    "Wooden train" : 250,
    "Teddy bear" : 300,
    "Bicycle" : 400
}

is_task_done = False

crafted_presents = {}

materials = list(map(int, input().split(" ")))
magic_level = deque(map(int, input().split(" ")))

while materials and magic_level:
    if materials[-1] == 0 and magic_level[0] == 0:
        materials.pop()
        magic_level.popleft()
        continue

    if materials[-1] == 0:
        materials.pop()
        continue

    if magic_level[0] == 0:
        magic_level.popleft()
        continue

    last_box = materials.pop()
    magic = magic_level.popleft()
    total_magic_level = last_box * magic

    if total_magic_level in presents_info.values():
        present = next(key for key, value in presents_info.items() if value == total_magic_level)
        if present not in crafted_presents:
            crafted_presents[present] = 1
        else:
            crafted_presents[present] += 1
    elif total_magic_level < 0:
        total_magic_level = last_box + magic
        materials.append(total_magic_level)
    else:
        total_magic_level = last_box + 15
        materials.append(total_magic_level)

if "Doll" in crafted_presents.keys() and "Wooden train" in crafted_presents.keys():
    if crafted_presents["Doll"] >= 1 and crafted_presents["Wooden train"] >= 1:
        is_task_done = True
elif "Teddy bear" in crafted_presents.keys() and "Bicycle" in crafted_presents.keys():
    if crafted_presents["Teddy bear"] >= 1 and crafted_presents["Bicycle"] >= 1:
        is_task_done = True

if is_task_done:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print("Materials left:", end=" ")
    print(", ".join(map(str, reversed(materials))))

if magic_level:
    print("Magic left:", end=" ")
    print(", ".join(map(str, magic_level)))

for toy in sorted(crafted_presents):
    print(f"{toy}: {crafted_presents[toy]}")