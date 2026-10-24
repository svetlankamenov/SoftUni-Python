total_cost = 0.0
city_name = input()
packet_type = input()
vip_discount = input()
days_count = int(input())

if days_count < 1:
    print("Days must be positive number!")
else:
    if days_count > 7:
        days_count -= 1

    if (city_name == "Bansko" or city_name == "Borovets"):

        if packet_type == "withEquipment":
            total_cost = days_count * 100.00
            if vip_discount == "yes":
                total_cost *= 0.90
            print(f"The price is {total_cost:.2f}lv! Have a nice time!")

        elif packet_type == "noEquipment":
            total_cost = days_count * 80.00
            if vip_discount == "yes":
                total_cost *= 0.95
            print(f"The price is {total_cost:.2f}lv! Have a nice time!")
        else:
            print("Invalid input!")

    elif (city_name == "Varna" or city_name == "Burgas"):

        if packet_type == "withBreakfast":
            total_cost = days_count * 130.00
            if vip_discount == "yes":
                total_cost *= 0.88
            print(f"The price is {total_cost:.2f}lv! Have a nice time!")
        elif packet_type == "noBreakfast":
            total_cost = days_count * 100.00
            if vip_discount == "yes":
                total_cost *= 0.93
            print(f"The price is {total_cost:.2f}lv! Have a nice time!")
        else:
            print("Invalid input!")

    else:
        print("Invalid input!")