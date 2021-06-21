items = input().split("!")
command = input()

while command != "Go Shopping!":
    tokens = command.split(" ")
    if tokens[0] == "Urgent":
        item = tokens[1]
        if item in items:
            command = input()
            continue
        else:
            items.insert(0, item)

    elif tokens[0] == "Unnecessary":
        item = tokens[1]
        if item in items:
            items.remove(item)

    elif tokens[0] == "Correct":
        old_item = tokens[1]
        new_item = tokens[2]

        if old_item in items:
            idx = items.index(old_item)
            items[idx] = new_item
        else:
            command = input()
            continue
    elif tokens[0] == "Rearrange":
        item = tokens[1]
        if item in items:
            idx = items.index(item)
            temp = items.pop(idx)
            items.append(temp)

    command = input()


print(", ".join(items))