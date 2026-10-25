def loading_bar(num: int):
    bar = []
    if num == 100:
        bar.append("%"*10)
        print("100% Complete!")
        print("[", end="")
        for char in bar:
            print(char, end="")
        print("]")
    else:
        bar.append("%"*(num//10))
        bar.append("."*(10 - (num//10)))
        print(f"{num}% ", end="")
        print("[", end="")
        for char in bar:
            print(char, end="")
        print("]")
        print("Still loading...")

number = int(input())
loading_bar(number)