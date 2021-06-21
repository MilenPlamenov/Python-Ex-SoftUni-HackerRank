number_of_command = int(input())
houses = input().split(" ")
current_position = 0
for i in range(len(houses)):
    houses[i] = int(houses[i])
for i in range(number_of_command):
    command = input().split(" ")
    if command[0] == "Forward":
        number_of_steps = int(command[1])
        if current_position + number_of_steps < len(houses):
            current_position += number_of_steps
            houses.pop(current_position)

    elif command[0] == "Back":
        number_of_steps = int(command[1])
        if current_position - number_of_steps >= 0:
            current_position -= number_of_steps
            houses.pop(current_position)

    elif command[0] == "Gift":
        index = int(command[1])
        house_number = int(command[2])
        if 0 <= index < len(houses):
            houses.insert(index, house_number)
            current_position = index

    elif command[0] == "Swap":
        number_one = int(command[1])
        number_two = int(command[2])
        if number_one in houses and number_two in houses:
            index_one = houses.index(number_one)
            index_two = houses.index(number_two)
            houses[index_one] = number_two
            houses[index_two] = number_one
    else:
        continue

print(f"Position: {current_position}")
houses_str = []
for house in houses:
    houses_str.append(str(house))
print(', '.join(houses_str))
