name = input()
data = input()

while True:
    password = input()
    if password == data:
        print(f"Welcome {name}!")
        break