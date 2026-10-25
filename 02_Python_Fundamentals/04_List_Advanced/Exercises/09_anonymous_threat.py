def merge_elements(start_index: int, end_index: int, elements: list):
    start_index = max(0, start_index)
    end_index = min(len(elements) - 1, end_index)
    temporary_lst = []

    if start_index > end_index:
        return elements
    else:
        if start_index != 0:
            for i in range(0, start_index):
                temporary_lst.append(elements[i])

        new_element = "".join(elements[start_index:end_index+1])
        temporary_lst.append(new_element)

        for i in range(end_index+1, len(elements)):
            temporary_lst.append(elements[i])

        return temporary_lst

def divide_element(index: int, parts: int, elements: list):
    temporary_lst = []

    for i in range(0, index):
        temporary_lst.append(elements[i])

    element = elements[index]

    if len(element) % parts == 0:
        length = len(element) // parts
        temporary_lst.extend([element[i:i+length] for i in range(0, len(element), length)])
    else:
        length = len(element) // parts
        begin = 0

        for i in range(parts-1):
            temporary_lst.append(element[begin:begin+length])
            begin += length

        temporary_lst.append(element[begin:])


    for j in range(index + 1, len(elements)):
        temporary_lst.append(elements[j])

    return temporary_lst

strings = input().split(" ")

while True:
    command = input()
    if command == "3:1":
        print(*strings)
        break

    command = command.split(" ")

    if command[0] == "merge":
        strings = merge_elements(int(command[1]), int(command[2]), strings)
    elif command[0] == "divide":
        strings = divide_element(int(command[1]), int(command[2]), strings)