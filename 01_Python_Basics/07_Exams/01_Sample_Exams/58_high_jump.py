target_height = int(input())
new_target = target_height - 30
total_jumps = 0
failures = 0
jump = 0

while True:

    for _ in range(3):
        jump = int(input())
        if jump > new_target:
            total_jumps += 1
            new_target += 5
            break
        elif jump <= new_target:
            total_jumps += 1
            failures += 1


    if new_target > target_height:
        print(f"Tihomir succeeded, he jumped over {target_height}cm after {total_jumps} jumps.")
        break

    if failures == 3:
        print(f"Tihomir failed at {new_target}cm after {total_jumps} jumps.")
        break
    else:
        failures = 0