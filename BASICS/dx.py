target = 10000
total_steps = 0
command = input()
goal_reach = False
while command != "Going home":
    current_steps =int(command)
    total_steps += current_steps
    if total_steps >= target:
        goal_reach = True
        break
    command = input()
if command == "Going home":
    last_steps = int(input())
    total_steps += last_steps
    if total_steps >= target:
        goal_reach = True
diff = abs(total_steps - target)
if goal_reach:
        print(f"Goal reached! Good job!")
        print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
