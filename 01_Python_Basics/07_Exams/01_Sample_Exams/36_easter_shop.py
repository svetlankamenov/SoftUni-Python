initial_quantity_eggs = int(input())
sold_eggs = 0

while True:
    action = input()

    if action == "Close":
        print("Store is closed!")
        print(f"{sold_eggs} eggs sold.")
        break

    eggs_count = int(input())

    if action == "Buy":
        if eggs_count > initial_quantity_eggs:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {initial_quantity_eggs}.")
            break
        sold_eggs += eggs_count
        initial_quantity_eggs -= eggs_count

    elif action == "Fill":
        initial_quantity_eggs += eggs_count