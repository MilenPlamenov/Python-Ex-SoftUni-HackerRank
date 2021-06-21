targets = [int(i) for i in input().split()]

command = input()
while command != "End":
    args = command.split()
    new_command = args[0]
    if new_command == "Shoot":
        index = int(args[1])
        power = int(args[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif new_command == "Add":
        index = int(args[1])
        value = int(args[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif new_command == "Strike":
        index = int(args[1])
        radius_one = index - int(args[2])
        radius_two = index + int(args[2])
        if 0 <= index < len(targets):
            if radius_one >= 0 and radius_two < len(targets):
                del targets[radius_one:radius_two + 1]
            else:
                print("Strike missed!")
    command = input()

targets = [str(i) for i in targets]
print("|".join(targets))
