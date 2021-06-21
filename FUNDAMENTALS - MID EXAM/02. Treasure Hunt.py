data = input().split("|")
command = input()
while command != "Yohoho!":
    if "Loot" in command:
        command = command.split(" ")
        command = command[1:]
        for item in command:
            if item not in data:
                data.insert(0,item)
    elif "Drop" in command:
        command = command.split()
        index = int(command[1])
        if 0 <= index < len(data):
            data.append(data.pop(index))

    elif "Steal" in command:
        command = command.split()
        index = int(command[1])
        if index >= len(data):
            print(', '.join(data))
            data = []
        elif 0 <= index < len(data):
            print(', '.join(data[len(data)-index:]))
            del data[len(data) - index:]
    command = input()
if data:
    average = sum([len(element) for element in data]) / len(data)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")