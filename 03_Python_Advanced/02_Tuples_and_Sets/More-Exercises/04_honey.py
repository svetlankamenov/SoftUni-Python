from collections import deque

total_honey = 0

working_bees = deque(list(map(int, input().split())))
collected_nectar = list(map(int, input().split()))
symbols = deque(input().split(" "))

while working_bees and collected_nectar:
    bee_value = working_bees.popleft()
    nectar = collected_nectar.pop()

    if nectar >= bee_value:
        symbol = symbols.popleft()
        if symbol == "+":
            total_honey += abs(bee_value + nectar)
        elif symbol == "-":
            total_honey += abs(bee_value - nectar)
        elif symbol == "*":
            total_honey += abs(bee_value * nectar)
        elif symbol == "/" and nectar != 0:
            total_honey += abs(bee_value / nectar)
    else:
        working_bees.appendleft(bee_value)
        continue

print(f"Total honey made: {total_honey}")

if working_bees:
    print(f"Bees left:", end=" ")
    print(", ".join(map(str, working_bees)))

if collected_nectar:
    print(f"Nectar left:", end=" ")
    print(", ".join(map(str, collected_nectar)))