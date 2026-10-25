n = int(input())

for _ in range(n):
    message = int(input())

    if message == 88:
        print("Hello")
    elif message == 86:
        print("How are you?")
    elif message < 88 and message != 88 and message != 86:
        print("GREAT!")
    elif message > 88:
        print("Bye.")