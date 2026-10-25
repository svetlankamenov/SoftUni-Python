electron_shell = []
layer = 1

electrons_count = int(input())

while electrons_count > 0:
    possible_electrons_count = 2 * (layer ** 2)

    if possible_electrons_count - electrons_count > 0:
        electron_shell.append(electrons_count)
        electrons_count = 0
    else:
        electron_shell.append(possible_electrons_count)
        electrons_count -= possible_electrons_count

    layer += 1

print(electron_shell)