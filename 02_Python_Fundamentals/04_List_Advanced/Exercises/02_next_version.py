version_data = input().split(".")
version_data = list(map(int, version_data))

version_data[2] += 1

if version_data[2] > 9:
    version_data[2] = 0
    version_data[1] += 1

if version_data[1] > 9:
    version_data[1] = 0
    version_data[0] += 1

print(f"{version_data[0]}.{version_data[1]}.{version_data[2]}")