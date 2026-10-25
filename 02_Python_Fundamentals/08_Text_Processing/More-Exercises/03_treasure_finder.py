from math import ceil

def decrypt_message(messages: list, keys: str):
    keys = list(map(int, keys.split(" ")))
    for message in messages:
        decrypted_message = ""
        key = keys * ceil(len(message) / len(keys))

        for i in range (0, len(message)):
            decrypted_message += chr(ord(message[i]) - key[i])

        treasure_type = decrypted_message.split("&")[1]
        start_index = decrypted_message.find("<")
        end_index = decrypted_message.find(">")
        coordinates = decrypted_message[start_index + 1:end_index]
        print(f"Found {treasure_type} at {coordinates}")

strings = []
numbers = input()

while True:
    line = input()
    if line == "find":
        break

    strings.append(line)

decrypt_message(strings, numbers)