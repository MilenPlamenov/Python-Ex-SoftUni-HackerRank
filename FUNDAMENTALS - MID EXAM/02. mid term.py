friends = input().split(", ")
blacklisted = []
lost_names = []
command = input()
while command != "Report":
    tokens = command.split()
    if tokens[0] == "Blacklist":
        name = tokens[1]
        if name in friends:
            print(f"{name} was blacklisted.")
            blacklisted.append(name)
            name_idx = friends.index(name)
            friends[name_idx] = "Blacklisted"
        else:
            print(f"{name} was not found.")

    elif tokens[0] == "Error":
        index = int(tokens[1])
        if 0 <= index < len(friends):
            if not friends[index] == "Blacklisted":
                if not friends[index] == "Lost":
                    print(f"{friends[index]} was lost due to an error.")
                    friends[index] = "Lost"
                    lost_names.append(friends[index])

    elif tokens[0] == "Change":
        index = int(tokens[1])
        new_name = tokens[2]
        if 0 <= index < len(friends):
            print(f"{friends[index]} changed his username to {new_name}.")
            friends[index] = new_name

    command = input()

print(f"Blacklisted names: {len(blacklisted)}")
print(f"Lost names: {len(lost_names)}")
print(f" ".join(friends))