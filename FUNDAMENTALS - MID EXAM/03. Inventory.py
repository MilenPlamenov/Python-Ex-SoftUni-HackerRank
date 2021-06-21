items = input().split(", ")
command = input()

while command != "Craft!":
    args = command.split(" - ")
    new_command = args[0]
    sec_arg = args[1]
    if new_command == "Collect":
        if sec_arg in items:
            command = input()
            continue
        else:
            items.append(sec_arg)

    elif new_command == "Drop":
        if sec_arg in items:
            items.remove(sec_arg)

    elif new_command == "Combine Items":
        sec_arg_token = sec_arg.split(":")
        old_item = sec_arg_token[0]
        new_item = sec_arg_token[1]
        if old_item in items:
            idx = items.index(old_item)
            items.insert(idx + 1, new_item)

    elif new_command == "Renew":
        if sec_arg in items:
            idx = items.index(sec_arg)
            temp = items.pop(idx)
            items.append(temp)

    command = input()

print(f", ".join(items))
