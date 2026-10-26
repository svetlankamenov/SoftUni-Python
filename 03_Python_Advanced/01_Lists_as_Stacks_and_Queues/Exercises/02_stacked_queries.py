stack = []

n = int(input())

for _ in range(n):
    command = input().split(" ")
    if command[0] == "1":
        stack.append(int(command[1]))
    elif command[0] == "2" and len(stack) > 0:
        stack.pop()
    elif command[0] == "3" and len(stack) > 0:
        print(max(stack))
    elif command[0] == "4" and len(stack) > 0:
        print(min(stack))

ordered_stack = []

for _ in range(len(stack)):
    ordered_stack.append(stack.pop())

print(", ".join(map(str, ordered_stack)))