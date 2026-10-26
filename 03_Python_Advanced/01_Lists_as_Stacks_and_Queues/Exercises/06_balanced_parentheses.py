from collections import deque

opening_symbols = []
is_balanced = False

string = deque(input())

while len(string) != 0:
    symbol = string.popleft()
    if symbol != ")" and symbol != "]" and symbol != "}":
        opening_symbols.append(symbol)
    else:
        if len(opening_symbols) == 0:
            is_balanced = False
            break

        last_opening_symbol = opening_symbols.pop()
        if symbol == ")":
            if last_opening_symbol == "(":
                is_balanced = True
            else:
                is_balanced = False
                break
        elif symbol == "]":
            if last_opening_symbol == "[":
                is_balanced = True
            else:
                is_balanced = False
                break
        elif symbol == "}":
            if last_opening_symbol == "{":
                is_balanced = True
            else:
                is_balanced = False
                break

if is_balanced and len(opening_symbols) == 0:
    print("YES")
else:
    print("NO")