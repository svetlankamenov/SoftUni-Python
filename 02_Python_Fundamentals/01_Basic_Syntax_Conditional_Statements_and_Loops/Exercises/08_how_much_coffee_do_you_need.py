coffees_count = 0

while True:
    event = input()
    if event == "END":
        if coffees_count <= 5:
            print(coffees_count)
            break
        else:
            print("You need extra sleep")
            break

    if event in ("coding", "dog", "cat", "movie"):
        coffees_count += 1
    elif event in ("CODING", "DOG", "CAT", "MOVIE"):
        coffees_count += 2
    else:
        continue