pirate_ship = list(map(int,input().split(">")))
warship = list(map(int,input().split(">")))
maximum_hp_capacity = int(input())
command = input()
stalemate = True
while command != "Retire":
    command = command.split(" ")
    if command[0] == "Fire":
        index, damage = int(command[1]), int(command[2])
        if 0<= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                stalemate = False
                break
    elif command[0] == "Defend":
        start, end, damage = int(command[1]), int(command[2]), int(command[3])
        if 0 <= start <= end < len(pirate_ship):
            for section in range(start,end+1):
                pirate_ship[section] -= damage
                if pirate_ship[section] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    stalemate = False
                    break

    elif command[0] == "Repair":
        index, hp = int(command[1]), int(command[2])
        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += hp
            if pirate_ship[index] > maximum_hp_capacity:
                pirate_ship[index] = maximum_hp_capacity

    elif command[0] == "Status":
        count = 0
        for section in pirate_ship:
            if section < maximum_hp_capacity/5:
                count += 1
        print(f"{count} sections need repair.")
        # print(len([section for section in pirate_ship if section < maximum_hp_capacity/5]))
    command = input()
if stalemate:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")