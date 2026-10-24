steps_goal = 10000
steps_made = 0

while steps_made < steps_goal:
    action = input()

    if action == "Going home":
        action = input()
        action = int(action)
        steps_made += action

        if steps_made > steps_goal:
            print("Goal reached! Good job!")
            print(f"{abs(steps_made - steps_goal)} steps over the goal!")
            break
        else:
            print(f"{abs(steps_made - steps_goal)} more steps to reach goal.")
            break

    action = int(action)
    steps_made += action

    if steps_made >= steps_goal:
        print("Goal reached! Good job!")
        print(f"{abs(steps_made - steps_goal)} steps over the goal!")
        break