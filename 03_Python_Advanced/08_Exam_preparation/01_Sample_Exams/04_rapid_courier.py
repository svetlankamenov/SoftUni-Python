from collections import deque

total_delivered_weight = 0

packages_weight = [int(x) for x in input().split()]
couriers_capacities = deque([int(x) for x in input().split()])

while packages_weight and couriers_capacities:
    courier = couriers_capacities.popleft()
    package = packages_weight.pop()

    if courier >= package:
        total_delivered_weight += package
        courier -= 2 * package
        if courier > 0:
            couriers_capacities.append(courier)
    else:
        package -= courier
        total_delivered_weight += courier
        packages_weight.append(package)

print(f"Total weight: {total_delivered_weight} kg")
if len(packages_weight) == 0 and len(couriers_capacities) == 0:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif len(packages_weight) != 0 and len(couriers_capacities) == 0:
    print("Unfortunately, there are no more available couriers to deliver the following packages:", end=" ")
    print(", ".join(map(str, packages_weight)))
elif len(couriers_capacities) != 0 and len(packages_weight) == 0:
    print("Couriers are still on duty:", end=" ")
    print(", ".join(map(str, couriers_capacities)), end=" ")
    print("but there are no more packages to deliver.")