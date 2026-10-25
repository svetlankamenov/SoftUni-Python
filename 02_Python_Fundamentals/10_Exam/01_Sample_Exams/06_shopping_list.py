def correct_item(old: str, new: str, lst: list):
    if old in lst:
        index = lst.index(old)
        lst[index] = new
        return lst
    else:
        return lst

def rearrange_item(item:str, lst: list):
    if item in lst:
        lst.remove(item)
        lst.append(item)
        return lst
    else:
        return lst

initial_list = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        print(", ".join(initial_list))
        break

    command = command.split(" ")

    if command[0] == "Urgent":
        if command[1] not in initial_list:
            initial_list.insert(0, command[1])
    elif command[0] == "Unnecessary":
        if command[1] in initial_list:
            initial_list.remove(command[1])
    elif command[0] == "Correct":
        initial_list = correct_item(command[1], command[2], initial_list)
    elif command[0] == "Rearrange":
        initial_list = rearrange_item(command[1], initial_list)