def boarding_passengers(capacity: int, *args):
    boarding_details = {}
    all_boarded = True
    output = ""

    for passenger in args:
        capacity_needed, name = passenger
        if capacity_needed <= capacity:
            if name not in boarding_details:
                boarding_details[name] = capacity_needed
            else:
                boarding_details[name] += capacity_needed
            capacity -= capacity_needed
        else:
            all_boarded = False

    boarding_details = dict(sorted(boarding_details.items(),key=lambda x: (-x[1], x[0])))

    output += "Boarding details by benefit plan:\n"
    for name, people in boarding_details.items():
        output += f"## {name}: {people} guests\n"

    if all_boarded:
        output += "All passengers are successfully boarded!"
    else:
        if capacity == 0:
            output += "Boarding unsuccessful. Cruise ship at full capacity."
        else:
            output += f"Partial boarding completed. Available capacity: {capacity}."

    return output

print(boarding_passengers(150, (35,'Diamond'), (55, 'Platinum'), (35,'Gold'), (25, 'First Cruiser')))