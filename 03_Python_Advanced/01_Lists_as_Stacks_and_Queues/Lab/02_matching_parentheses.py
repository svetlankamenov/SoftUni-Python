expression = input()
expression = list(expression)
starting_indices = []

for i in range(len(expression)):
    if expression[i] == "(":
        starting_indices.append(i)
    elif expression[i] == ")":
        start_index = starting_indices.pop()
        print("".join(expression[start_index:i+1]))