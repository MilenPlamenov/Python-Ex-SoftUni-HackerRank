command = input()
city_gold = {}
city_populations = {}
while command != "Sail":
    command = command.split("||")
    city = command[0]
    population = int(command[1])
    gold = int(command[2])
    if city not in city_gold:
        city_gold[city] = gold
        city_populations[city] = population
    else:
        city_gold[city] += gold
        city_populations[city] += population
    command = input()

while command != "End":
    command = command.split("=>")
    if command[0] == "Plunder":
        town = command[1]
        people = int(command[2])
        gold = int(command[3])
        if town in city_gold:
            city_gold[town] -= gold
            city_populations[town] -= people
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            if city_gold[town] == 0 or city_populations[town] == 0:
                city_gold.pop(town)
                city_populations.pop(town)
                print(f"{town} has been wiped off the map!")
    elif command[0] == "Prosper":
        town = command[1]
        gold = int(command[2])
        if town in city_gold:
            if gold < 0:
                print("Gold added cannot be a negative number!")
            else:
                city_gold[town] += gold
                print(f"{gold} gold added to the city treasury. {town} now has {city_gold[town]} gold.")
    command = input()

if len(city_gold) > 0:
    print(f"Ahoy, Captain! There are {len(city_gold)} wealthy settlements to go to:")
    for city, gold in sorted(city_gold.items(), key=lambda x: (x[1], -ord(x[0][0])), reverse=True):  # <-- sorted by gold in descending order, then by their name in ascending order.
        print(f"{city} -> Population: {city_populations[city]} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")