n = int(input())
plant_rarity = {}
new_dict = {}
for _ in range(n):
    plant, rarity = input().split("<->")
    if plant not in plant_rarity:
        plant_rarity[plant] = []
        ratings = []
        plant_rarity[plant].append(int(rarity)) # 0 index
        plant_rarity[plant].append(ratings) # 1 index
    else:
        plant_rarity[plant].remove(plant_rarity[plant][0])
        plant_rarity[plant].insert(0, int(rarity))

command = input()

while command != "Exhibition":
    command = command.split(': ')
    if command[0] == "Rate":
        new = command[1].split(" - ")
        plant = new[0]
        rating = int(new[1])
        if plant in plant_rarity:
            plant_rarity[plant][1].append(rating)
        else:
            print("error")
    elif command[0] == "Update":
        new = command[1].split(" - ")
        plant = new[0]
        new_rarity = int(new[1])
        if plant in plant_rarity:
            plant_rarity[plant][0] = new_rarity
        else:
            print("error")
    elif command[0] == "Reset":
        new = command[1].split(" - ")
        plant = new[0]
        if plant in plant_rarity:
            plant_rarity[plant][1].clear()
        else:
            print("error")
    else:
        print("error")
    command = input()
for plant, rating in plant_rarity.items():
    if len(plant_rarity[plant][1]) != 0:
        average = sum([c for c in plant_rarity[plant][1]]) / len(plant_rarity[plant][1])
    else:
        average = 0
    new_dict[plant] = [rating[0], average]
print("Plants for the exhibition:")
for plant, rarity in sorted(new_dict.items(), key=lambda x: (x[1][0], x[1][1]), reverse=True):
    print(f"- {plant}; Rarity: {new_dict[plant][0]}; Rating: {new_dict[plant][1]:.2f}")

