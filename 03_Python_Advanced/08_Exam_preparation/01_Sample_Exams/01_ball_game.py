from collections import deque

total_goals = 0

strength = [int(x) for x in input().split()]
accuracy = deque([int(x) for x in input().split()])

while strength and accuracy:
    s = strength.pop()
    a = accuracy.popleft()
    result = s + a

    if result == 100:
        total_goals += 1
    elif result < 100:
        if s < a:
            accuracy.appendleft(a)
        elif s > a:
            strength.append(s)
        else:
            strength.append(result)
    else:
        s -= 10
        strength.append(s)
        accuracy.append(a)

if total_goals == 3:
    print("Paul scored a hat-trick!")
elif total_goals > 3:
    print("Paul performed remarkably well!")
elif 0 < total_goals < 3:
    print("Paul failed to make a hat-trick.")
else:
    print("Paul failed to score a single goal.")

if total_goals != 0:
    print(f"Goals scored: {total_goals}")

if strength:
    print("Strength values left: ", end="")
    print(", ".join(map(str, strength)))

if accuracy:
    print("Accuracy values left: ", end="")
    print(", ".join(map(str, accuracy)))