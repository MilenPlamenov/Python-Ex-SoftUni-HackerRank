gifts = input().split(" ")

command = input()
while command != "No Money":
    tokens = command.split(" ")
    if tokens[0] == "OutOfStock":
        gift = tokens[1]
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = "None"

    elif tokens[0] == "Required":
        index = int(tokens[2])
        if index >= 0 and index < len(gifts):
            gifts[index] = tokens[1]

    elif tokens[0] == "JustInCase":
        gifts[-1] = tokens[1]

    command = input()

res = []
for gift in gifts:
    if gift != "None":
        res.append(gift)


print(" ".join(res))