array = [int(i) for i in input().split()]

command = input()

while command != "end":
    new_command = command.split(" ")
    if new_command[0] == "swap":
        index_one = int(new_command[1])
        index_two = int(new_command[2])
        array[index_one], array[index_two] = array[index_two], array[index_one] #index swap <-

    elif new_command[0] == "multiply":
        index_one = int(new_command[1])
        index_two = int(new_command[2])
        array[index_one] *= array[index_two]

    elif new_command[0] == "decrease":
        array = [int(i) - 1 for i in array]

    command = input()

print(", ".join(str(x) for x in array))