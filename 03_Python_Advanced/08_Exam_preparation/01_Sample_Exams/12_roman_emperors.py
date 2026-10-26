def list_roman_emperors(*args, **kwargs):
    successful_emperors = {}
    unsuccessful_emperors = {}
    output = ""

    for emperor in args:
        name, success = emperor
        if success:
            successful_emperors[name] = kwargs[name]
        else:
            unsuccessful_emperors[name] = kwargs[name]

    successful_emperors = dict(sorted(successful_emperors.items(), key=lambda x: (-x[1], x[0])))
    unsuccessful_emperors = dict(sorted(unsuccessful_emperors.items(), key=lambda x: (x[1], x[0])))

    output += f"Total number of emperors: {(len(successful_emperors)+len(unsuccessful_emperors))}\n"

    if successful_emperors:
        output += "Successful emperors:\n"
        for emperor_name, years in successful_emperors.items():
            output += f"****{emperor_name}: {years}\n"

    if unsuccessful_emperors:
        output += "Unsuccessful emperors:\n"
        for emperor_name, years in unsuccessful_emperors.items():
            output += f"****{emperor_name}: {years}\n"

    output = output.rstrip()

    return output