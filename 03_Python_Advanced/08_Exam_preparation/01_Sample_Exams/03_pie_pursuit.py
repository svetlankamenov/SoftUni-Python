from collections import deque

contestants = deque(int(x) for x in input().split())
pies = [int(x) for x in input().split()]

while contestants and pies:
    contestant = contestants.popleft()
    pie = pies.pop()

    if contestant >= pie:
        contestant -= pie
        if contestant > 0:
            contestants.append(contestant)
    else:
        pie -= contestant
        if pie > 1:
            pies.append(pie)
        elif pie == 1:
            if len(pies) >= 1:
                next_pie = pies.pop()
                next_pie += pie
                pies.append(next_pie)
            else:
                pies.append(pie)

if not contestants and not pies:
    print("We have a champion!")
elif not pies and contestants:
    print("We will have to wait for more pies to be baked!")
    print("Contestants left: ", end="")
    print(", ".join(map(str, contestants)))
elif not contestants and pies:
    print("Our contestants need to rest!")
    print("Pies left: ", end="")
    print(", ".join(map(str, pies)))