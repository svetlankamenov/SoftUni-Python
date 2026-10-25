free_chairs_count = 0
flag = True
rooms_count = int(input())

for room in range(1, rooms_count+1):
    chairs, visitors = input().split(" ")
    if len(chairs) - int(visitors) < 0:
        print(f"{abs(len(chairs) - int(visitors))} more chairs needed in room {room}")
        flag = False
    else:
        free_chairs_count += abs(len(chairs) - int(visitors))
if flag:
    print(f"Game On, {free_chairs_count} free chairs left")