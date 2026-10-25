resources = {}
counter = 0
last_resource = ""

while True:
    counter += 1
    line = input()

    if line == "stop":
        for resource, quantity in resources.items():
            print(f"{resource} -> {quantity}")
        break

    if counter % 2 != 0:
        last_resource = line
    else:
        if last_resource not in resources:
            resources[last_resource] = int(line)
        else:
            resources[last_resource] += int(line)