import os

def create_a_file(file_name:str):
    file = open(file_name, "w")
    file.close()

def add_content_to_file(file_name:str, content:str):
    with open(file_name, "a") as file:
        file.write(content + "\n")

def replace_content_in_file(file_name:str, old_string:str, new_string:str):
    try:
        with open(file_name, "r") as file:
            text = file.read()

        text = text.replace(old_string, new_string)

        with open(file_name, "w") as file:
            file.write(text)

    except FileNotFoundError:
        print("An error occurred")

def delete_file(file_name:str):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("An error occurred")


while True:
    command = input().split("-")
    if command[0] == "End":
        break

    if command[0] == "Create":
        create_a_file(command[1])
    elif command[0] == "Add":
        add_content_to_file(command[1], command[2])
    elif command[0] == "Replace":
        replace_content_in_file(command[1], command[2], command[3])
    elif command[0] == "Delete":
        delete_file(command[1])