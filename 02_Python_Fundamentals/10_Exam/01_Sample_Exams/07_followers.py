def add_new_follower(name: str, info: dict):
    if name not in info.keys():
        info[name] = {"Likes" : 0, "Comments": 0}

    return info

def add_likes(name: str, count: int, info: dict):
    if name not in info.keys():
        info[name] = {"Likes" : count, "Comments": 0}
    else:
        info[name]["Likes"] += count

    return info

def add_comments(name: str, info: dict):
    if name not in info.keys():
        info[name] = {"Likes" : 0, "Comments": 1}
    else:
        info[name]["Comments"] += 1

    return info

def block_user(name: str, info: dict):
    if name not in info.keys():
        print(f"{name} doesn't exist.")
    else:
        del info[name]

    return info

def print_followers(info: dict):
    print(f"{len(info)} followers")
    for follower in info.keys():
        print(f"{follower}: {info[follower]['Likes']+info[follower]['Comments']}")

facebook_info = {}

while True:
    command = input()
    if command == "Log out":
        print_followers(facebook_info)
        break

    command = command.split(": ")

    if command[0] == "New follower":
        facebook_info = add_new_follower(command[1], facebook_info)

    elif command[0] == "Like":
        facebook_info = add_likes(command[1], int(command[2]), facebook_info)

    elif command[0] == "Comment":
        facebook_info = add_comments(command[1], facebook_info)

    elif command[0] == "Blocked":
        facebook_info = block_user(command[1], facebook_info)