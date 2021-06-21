events = input().split("|")

energy = 100
coins = 100

isBankrupt = False

for event in events:
    arguments = event.split("-")
    name = arguments[0]
    number = int(arguments[1])
    if name == "rest":
        gained_energy = 0
        if energy + number <= 100:
            energy += number
            gained_energy = number
        else:
            gained_energy = 100 - energy
            energy = 100
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif name == "order":
        if energy - 30 >= 0:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        if coins - number > 0:
            coins -= number
            print(f"You bought {name}.")
        else:
            isBankrupt = True
            print(f"Closed! Cannot afford {name}.")
            break

if not isBankrupt:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")