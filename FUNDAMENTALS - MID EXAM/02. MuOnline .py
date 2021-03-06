dungeon_rooms = input().split("|")
health = 100
bitcoin = 0
is_dead = False
room_counter = 0
for room in dungeon_rooms:
    room_counter += 1
    arguments = room.split(" ")
    command = arguments[0]
    number = int(arguments[1])
    if command == "potion":
        gained_health = 0
        if health + number < 100:
            gained_health += number
            health += gained_health
        else:
            gained_health = 100 - health
            health = 100
        print(f"You healed for {gained_health} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoin += number
        print(f'You found {number} bitcoins.')
    else:
        attack_of_the_monster = number
        health -= attack_of_the_monster
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            is_dead = True
            print(f"Best room: {room_counter}")
            break


if not is_dead:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {health}")

