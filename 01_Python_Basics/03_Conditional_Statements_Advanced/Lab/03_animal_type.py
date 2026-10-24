animal = input()

if animal.lower() == "dog":
    print("mammal")
elif (animal.lower() == "crocodile" or animal.lower() == "tortoise"
      or animal.lower() == "snake"):
    print("reptile")
else:
    print("unknown")