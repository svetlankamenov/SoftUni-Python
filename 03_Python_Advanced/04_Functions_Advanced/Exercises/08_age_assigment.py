def age_assignment(*args, **kwargs):
    people = {}

    for letter in kwargs:
        for person in args:
            if letter in person:
                people[person] = kwargs[letter]

    people = dict(sorted(people.items(), key=lambda x: x[0]))

    result = "\n".join(f"{person} is {age} years old." for person, age in people.items())

    return result

print(age_assignment("Amy", "Bill", "Willy", W=36,A=22, B=61))