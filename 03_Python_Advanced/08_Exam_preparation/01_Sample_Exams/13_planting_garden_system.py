def plant_garden(available_space:float, *args, **kwargs):
    all_planted = True
    output = ""
    garen = {}
    allowed_plants = {name: space for name, space in args}
    kwargs = dict(sorted(kwargs.items(), key=lambda x: x[0]))

    for plant, count in kwargs.items():
        if plant in allowed_plants:
            space = allowed_plants[plant]
            for i in range(count, 0, -1):
                required_space = space * i
                if required_space <= available_space:
                    garen[plant] = i
                    available_space -= required_space
                    if count != i:
                        all_planted = False
                    break
            else:
                all_planted = False

    if all_planted:
        output += f"All plants were planted! Available garden space: {available_space:.1f} sq meters.\n"
    else:
        output += "Not enough space to plant all requested plants!\n"

    output += "Planted plants:\n"
    for plant, count in garen.items():
        output += f"{plant}: {count}\n"
    output = output.rstrip()

    return output