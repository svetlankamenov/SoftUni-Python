to_do_list = [0] * 10

while True:
    command = input()
    if command == "End":
        to_do_list = [note for note in to_do_list if note != 0]
        print(to_do_list)
        break

    command = command.split("-")

    if int(command[0]) < 1 or int(command[0]) > 10:
        continue

    to_do_list.pop(int(command[0]))
    to_do_list.insert(int(command[0]), command[1])